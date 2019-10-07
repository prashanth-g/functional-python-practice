import sys
sys.path.append('./src')

import pipeline

def test_pipeline():
    mobile_phones = [{'name': 'Redmi', 'country': 'India', 'active': True},
         {'name': 'Pixed', 'country': 'US', 'active': True},
         {'name': 'Windows', 'country': 'India', 'active': False}]
    result = pipeline.pipeline(mobile_phones, [pipeline.call(lambda x: 'Japan', 'country')])
    assert(list(result)[0].get('country') is 'Japan')

def test_pipeline_without_country_field():
    mobile_phones = [{'name': 'Redmi', 'active': True},
         {'name': 'Pixed', 'active': True},
         {'name': 'Windows', 'active': False}]
    result = pipeline.pipeline(mobile_phones, [pipeline.call(lambda x: 'Japan', 'country')])
    assert(list(result)[0].get('country') == 'Japan')




