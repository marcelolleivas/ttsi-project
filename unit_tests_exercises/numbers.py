
class Numbers:
    @staticmethod
    def is_unit(number: int) -> bool:
        """
        :param number: int
        :rtype: bool
        """
        unit = True
        if number > 9:
            unit = False
        return unit
