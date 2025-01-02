from api import get_all_valuations
from helpers import expand_valuations, normalize_input
from utils import BACKGROUND, BACKGROUND_MESSAGE
import pandas as pd
# FIXME: Get correct percentile
from scipy.stats import percentileofscore
# TODO: delete this later
import json
with open('./sample_input.json', 'r') as f:
    placeholder = json.load(f)



if __name__ == '__main__':
    valuations = get_all_valuations()
    # get all valuations
    valuation_history = pd.DataFrame(valuations)

    print('got all valuations')
    # expand valuations
    df = valuation_history.copy()
    df = expand_valuations(df)
    print('expanded valuations')

    # read input data
    input_data = normalize_input(placeholder)
    print('normalize output')

    # get set based on industry
    industry_set = df[df['primary_industry'] == input_data['industry']]

    # get sample based on record range
    rec_range_set = industry_set[industry_set['total_num_records'].between(
        input_data['total_records'][0], input_data['total_records'][1]
    )]

    # Calculate benchmarks
    average_valuation = industry_set['GBoost'].mean()
    print('average_valuation: ', average_valuation)
    min_valuation = industry_set['GBoost'].min()
    print('min_valuation: ', min_valuation)
    max_valuation = industry_set['GBoost'].max()
    print('max_valuation: ', max_valuation)
    top_25 = industry_set['GBoost'].quantile(0.75)
    print('top_25: ', top_25)

    ## percentile rank
    rank1 = percentileofscore(df['total_num_records'], input_data['total_records'][0], kind='rank')
    rank2 = percentileofscore(df['total_num_records'], input_data['total_records'][1], kind='rank')


    output = {
        'background_on_gulp': BACKGROUND,
        'background_on_the_method': BACKGROUND_MESSAGE,
        'valuation': {
            'average_valuation': f"${average_valuation:,.2f}",
            'min': f"${min_valuation:,.2f}",
            'max': f"${max_valuation:,.2f}",
            'top_25': f"${top_25:,.2f}"
        },
        'score': {
            'record_size': f"is between {input_data['total_records'][0]:,} and {input_data['total_records'][1]:,}",
            'data_length': f"{input_data['data_length']} years",
            'percentile_rank': f"ranks between {rank1:.2f}% and {rank2:.2f}% ",
            'quality_adjusted_score': f"{input_data['quality_score'] * 100:.2f}%"
        }
    }

    print(output)

    with open('./test.json', 'w') as f:
        json.dump(output, f)