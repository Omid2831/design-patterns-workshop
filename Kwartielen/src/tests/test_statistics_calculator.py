"""
TDD unit tests for StatisticsCalculator.

Expected values (hand-verified):

Brand A: 86,87,94,95,98,99,100,100,102,103,106,107,108,110,110,112,112,112,115,115
  mean   = 103.55   median = 104.5   mode = [112]   spread = 29
  Q1     = 98.5     Q2     = 104.5   Q3   = 111.0   IQR    = 12.5

Brand B: 55,82,86,94,95,100,101,103,105,106,107,109,110,113,113,116,117,119,124,132
  mean   = 104.35   median = 106.5   mode = [113]   spread = 77
  Q1     = 97.5     Q2     = 106.5   Q3   = 114.5   IQR    = 17.0
"""

import pytest
from Kwartielen.src.models.BatteryDataset import BatteryDataset
from Kwartielen.src.interfaces.IBasicStats import IBasicStats
from Kwartielen.src.interfaces.IQuartileStats import IQuartileStats
from Kwartielen.src.statistics.statistics_calculator import StatisticsCalculator

BRAND_A = [86, 87, 94, 95, 98, 99, 100, 100, 102, 103,
           106, 107, 108, 110, 110, 112, 112, 112, 115, 115]

BRAND_B = [55, 82, 86, 94, 95, 100, 101, 103, 105, 106,
           107, 109, 110, 113, 113, 116, 117, 119, 124, 132]


class TestStatisticsCalculatorInterface:
    """Verify StatisticsCalculator satisfies both interfaces (Liskov Substitution)."""

    def test_implements_ibasicstats(self):
        calc = StatisticsCalculator(BatteryDataset("X", [1, 2, 3]))
        assert isinstance(calc, IBasicStats)

    def test_implements_iquartilestats(self):
        calc = StatisticsCalculator(BatteryDataset("X", [1, 2, 3]))
        assert isinstance(calc, IQuartileStats)


class TestStatisticsCalculatorBrandA:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.calc = StatisticsCalculator(BatteryDataset("Brand A", BRAND_A))

    def test_mean(self):
        assert self.calc.mean() == pytest.approx(103.55)

    def test_median(self):
        assert self.calc.median() == pytest.approx(104.5)

    def test_mode(self):
        assert set(self.calc.mode()) == {112}

    def test_spread(self):
        assert self.calc.spread() == 29

    def test_quartile_1(self):
        assert self.calc.quartile(1) == pytest.approx(98.5)

    def test_quartile_2_equals_median(self):
        assert self.calc.quartile(2) == pytest.approx(104.5)

    def test_quartile_3(self):
        assert self.calc.quartile(3) == pytest.approx(111.0)

    def test_interquartile_range(self):
        assert self.calc.interquartile_range() == pytest.approx(12.5)

    def test_invalid_quartile_raises_value_error(self):
        with pytest.raises(ValueError):
            self.calc.quartile(4)


class TestStatisticsCalculatorBrandB:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.calc = StatisticsCalculator(BatteryDataset("Brand B", BRAND_B))

    def test_mean(self):
        assert self.calc.mean() == pytest.approx(104.35)

    def test_median(self):
        assert self.calc.median() == pytest.approx(106.5)

    def test_mode(self):
        assert set(self.calc.mode()) == {113}

    def test_spread(self):
        assert self.calc.spread() == 77

    def test_quartile_1(self):
        assert self.calc.quartile(1) == pytest.approx(97.5)

    def test_quartile_2_equals_median(self):
        assert self.calc.quartile(2) == pytest.approx(106.5)

    def test_quartile_3(self):
        assert self.calc.quartile(3) == pytest.approx(114.5)

    def test_interquartile_range(self):
        assert self.calc.interquartile_range() == pytest.approx(17.0)
