class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value: str):
        return int(value)

    def to_url(self, value: int):
        return '%04d' % value
