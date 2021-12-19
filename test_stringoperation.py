import pytest
from stringopertaion import StringOperation

class Test_StringOperation():
    stringvalue = "teaching at SDAacademy"

    def test_length_of_string(self):
        assert StringOperation(self.stringvalue).get_length() == 22

    def test_reverse_string(self):
        assert StringOperation(self.stringvalue).reverse_string() == self.stringvalue[::-1]

    def test_first_three_xters(self):
        assert StringOperation(self.stringvalue).first_three_characters() == 'tea'

    def test_get_last_foru_xters(self):
        assert StringOperation(self.stringvalue).last_four_characters() == 'demy'

    def test_characters_less_than_five(self):
        assert StringOperation('valu').first_three_characters() == None

    @pytest.mark.xfail
    def test_positional_not_int(self):
        assert StringOperation(self.stringvalue).get_postional_character('12') == 'S'

    def test_positional_raises_error(self):
        with pytest.raises(TypeError):
            StringOperation(self.stringvalue).get_postional_character('12')