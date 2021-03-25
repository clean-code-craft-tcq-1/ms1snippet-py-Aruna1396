import unittest

import sensor_validator
import math


class SensorValidatorTest(unittest.TestCase):

    def test_reports_error_for_abnormal_soc_readings(self):
        self.assertFalse(
            sensor_validator.validate_sensor_readings([0.0, 0.01, 0.5, 0.51], 'soc')
        )

    def test_reports_error_for_abnormal_current_readings(self):
        self.assertFalse(
            sensor_validator.validate_sensor_readings([0.03, 0.03, 0.03, 0.33], 'current')
        )

    def test_reports_error_for_invalid_input_sensor_entries(self):
        self.assertFalse((sensor_validator.validate_sensor_readings([], 'current')))
        self.assertFalse((sensor_validator.validate_sensor_readings([0.03, 0.03, 0.03, 0.33], 'temperature')))
        self.assertFalse((sensor_validator.validate_sensor_readings([math.nan, 0.03, 0.03, 0.33], 'soc')))

    def test_yields_positive_result_for_normal_sensor_readings(self):
        self.assertTrue((sensor_validator.validate_sensor_readings([0.0, 0.01, 0.02, 0.05], 'current')))
        self.assertTrue((sensor_validator.validate_sensor_readings([0.03, 0.035, 0.04, 0.045], 'soc')))


if __name__ == "__main__":
    unittest.main()
