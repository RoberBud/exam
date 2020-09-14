import source
import pytest 

class TestSource():

    def test_createList(self):
        t = source.Convert()
  
        input_dict = t.createList( {'hired': {'be': {'to': {'deserve': 'I'}}}})
        assert input_dict == ['hired', 'be', 'to', 'deserve', 'I']

    def test_listToDict(self):
        t = source.Convert()

        input_list = t.listToDict(['I', 'deserve', 'to', 'be', 'hired'])

        assert input_list == {'I': {'deserve': {'to': {'be': {'hired'}}}}}

    def test_combine(self):
        t = source.Convert()

        input_dict =  t.combine({'hired': {'be': {'to': {'deserve': 'I'}}}})

        assert input_dict == {'I': {'deserve': {'to': {'be': {'hired'}}}}}

