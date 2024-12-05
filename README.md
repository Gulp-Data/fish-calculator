# fish-calculator

Gathers detailed information about users, their company, and their data assets. The tool will use this input to calculate data valuations and scores based on patterns established from prior valuations. Includes detailed outputs summarizing the valuation and benchmarking the data's quality and potential by providing a percentile where the company lands compared to others.

## sample input

```json
{
  "user_info": {
    "full_name": "John Doe",
    "title": "Data Analyst",
    "email": "johndoe@example.com",
  },
  "company_info": {
    "company_name": "DataTech Inc.",
    "year_founded": "2015",
    "business_type": "B2B",
    "operating_locations": ["United States", "Canada", "Germany"],
    "main_industry": "Technology",
    "website": "https://www.datatech.com",
    "company_description": "Innovative data solutions for businesses.",
    "annual_revenue": "$50M-$100M",
    "employee_count": "201-500",
    "notable_customers": "BigTech Corp, FinancePro Ltd."
  },
  "data_info": {
    "year_began_collecting_data": "2018",
    "has_end_users": true,
    "end_user_count": 50000,
    "total_records": "10M-50M",
    "attributes_collected": "101-500",
    "collects_pii_or_phi": true,
    "cloud_providers": ["AWS", "Azure"],
    "monthly_cloud_bill": "$10K-$50K",
    "data_types_collected": ["Customer Data", "Behavioral Data", "Transaction Data"],
    "primary_data_usage": ["Marketing Analytics", "Customer Retention", "Product Development"],
    "data_valuation_update_frequency": "Quarterly"
  },
  "data_quality": {
    "duplication": 4,
    "depth": 5,
    "security": 3,
    "completeness": 4
  }
}
```

## sample output

### Background on Gulp

> 3,800+ valuations, $3B+ data valued, 3T+ records valued, 150K+ market comps behind the valuations

#### Background on the method

Our data value calculator leverages insights from previous valuations conducted by Gulp Data, focusing on data assets similar to yours. Unlike our market-comp models, which are based on actual market data and transactions, the data value calculator derives its insights from Gulp Data's prior in-house valuations of assets similar to yours. This method doesn’t rely on real-time market comparisons but instead applies patterns and valuation criteria we've established from assessing comparable data types. For a full data valuation, TEXT FISH to 1-800-iam-fish :)

### Data Valuation

Average data valuation of $870,976.00 with a min of X and max of Y. In your industry, companies in the top 25% of data value, had a minimum of 12,097,654 records.

### Data score

Between 60th and 82nd percentiles. IT companies with 1,096,800 records and 3 years of operating history, typically scored closer to the 60th percentile.
