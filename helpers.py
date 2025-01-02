import pandas as pd
from decimal import Decimal
from datetime import date
import numpy as np


def expand_valuations(valuations: pd.DataFrame) -> pd.DataFrame:
    '''
    expands the dataframe results and valuation to have a single
    layered dataframe.

    :valuations: datafrane containing gulps valuations history
    '''
    valuation_expanded = pd.json_normalize(
        valuations['valuation'].apply(
            lambda x: {k: v for k, v in x.items() if k not in ['Market', 'Cost']}))

    valuation_cost_expanded = pd.json_normalize(
        valuations['valuation'].apply(lambda x: x.get('Cost', {})))

    valuation_market_expanded = pd.json_normalize(
        valuations['valuation'].apply(lambda x: x.get('Market', {})))

    data_results_expanded = pd.json_normalize(valuations['data_results'])

    df = pd.concat(
        [valuations.drop(columns=['valuation', 'data_results']),
         valuation_expanded, valuation_cost_expanded,
         valuation_market_expanded, data_results_expanded], axis=1)

    return df


def text_to_num(text: str) -> int:
    '''
    provides numerical value to values that contain letters
    like: K, M or B
    :text: string that holds num value
    '''
    d = {
    'K': 3,
    'M': 6,
    'B': 9
    }
    if text[-1] in d:
        num, magnitude = text[:-1], text[-1]
        return int(Decimal(num) * 10 ** d[magnitude])
    else:
        return int(Decimal(text))


def clean_range(text: str) -> list:
    '''
    creates a list based on the string range
    :text: string seperated by '-'
    '''
    li = []
    for val in text.split('-'):
        li.append(text_to_num(val))
    return li


def data_length(year_began_collecting_data: str) -> int:
    '''
    finds the length of the data based on the given year
    :year_began_collecting_data: the year the company started
    collecting data
    '''
    current_date = date.today()
    current_year = current_date.year

    data_period = current_year - int(year_began_collecting_data)
    return data_period


def normalize_input(data: dict) -> dict:
    '''
    normalizes values from form to use in the correct format.
    :input_data: data to organize


    Input Data	        .......          Mapped Dataset Column

    ___________________________________________________________

    business_type	                 |->  business_type

    end_user_count                   |->  end_user_count

    attributes_collected	         |->  total_num_attributes

    total_records	                 |->  total_num_records

    year_began_collecting_data	     |->  data_start_date

    duplication, depth, completeness |->  record_dup_rate

    monthly_cloud_bill	             |->  data_costs

    primary_industry                 |->  industry

    '''
    num_att =  data['data_info']['attributes_collected'].split('-')
    quality_score = np.mean([
        data['data_quality']['duplication'],
        data['data_quality']['depth'],
        data['data_quality']['completeness']
        ]) / 5  # Normalize to 0-1 scale

    input_data = {
        "total_records": clean_range(data['data_info']['total_records']),
        "end_user_count":  data['data_info']['end_user_count'],
        "record_dup_rate": 1 - (data['data_quality']['duplication'] / 5),  # lower duplication = higher score
        "industry": data['company_info']['main_industry'],
        "data_length": data_length(data['data_info']['year_began_collecting_data']),
        "total_num_attributes": num_att,
        "quality_score": quality_score
    }

    return input_data
