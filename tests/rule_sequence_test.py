import sys
sys.path.append('./src')

import rule_sequence

def test_zero():
    result = rule_sequence.zero('010')
    assert(result == '10')

def test_zero_expect_none():
    result = rule_sequence.zero('110')
    assert(result == None)

def test_one():
    result = rule_sequence.one('110')
    assert(result == '10')

def test_one_expect_none():
    result = rule_sequence.one('010')
    assert(result == None)

def test_rule_sequence():
    functions = [rule_sequence.one, rule_sequence.zero]
    result = rule_sequence.rule_sequence('101', functions)
    assert(result == '1')

def test_rule_sequence_expects_none():
    functions = [rule_sequence.one, rule_sequence.zero]
    result = rule_sequence.rule_sequence('001', functions)
    assert(result == None)

def test_declarative_rule_sequence():
    functions = [rule_sequence.one, rule_sequence.zero]
    result = rule_sequence.declrative_rule_sequence('101', functions)
    assert(result == '1')

def test_eclarative_rule_sequence_expects_none():
    functions = [rule_sequence.one, rule_sequence.zero]
    result = rule_sequence.declrative_rule_sequence('001', functions)
    assert(result == None)
