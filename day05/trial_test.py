from day05_seq import statistics_NTP 

def test_counter_1():
    res = statistics_NTP("ACCTGXXCXXGTTACTGGGCXTTGTXX")
    assert res == {'A': 2, 'C': 5, 'G': 6, 'T': 7, 'Unknown': 7, 'Total': 27}




def test_counter_2():
    res = statistics_NTP("ACCGGGTTTT")
    assert res == {'A': 1, 'C': 2, 'G': 3, 'T': 4, 'Unknown': 0, 'Total': 10}