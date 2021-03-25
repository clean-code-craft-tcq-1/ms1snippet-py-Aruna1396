import math

SUPPORTED_CHARGING_PARAMETERS = {'soc', 'current'}

MAX_DELTA_VALUE = {'soc': 0.05, 'current': 0.1}

SENSOR_VALIDATOR_CODES = {0: 'INVALID_SENSOR_INPUTS',
                          1: 'VALID_SENSOR_INPUTS',
                          2: {'soc': 'SOC_SENSOR_OK', 'current': 'CURRENT_SENSOR_OK'},
                          3: {'soc': 'FAULTY_SOC_SENSOR', 'current': 'FAULTY_CURRENT_SENSOR'}
                          }


def is_sensor_readings_invalid(parameter_readings):
    if not is_sensor_reading_empty(parameter_readings):
        return is_NanValue_in_sensor_readings(parameter_readings)
    return True


def is_NanValue_in_sensor_readings(parameter_readings):
    if any([math.isnan(reading) for reading in parameter_readings]):
        return True
    return False


def is_sensor_reading_empty(parameter_readings):
    if len(parameter_readings) == 0:
        return True
    return False


def is_sensor_parameter_invalid(parameter_name):
    if parameter_name not in SUPPORTED_CHARGING_PARAMETERS:
        return True
    return False


def validate_input_sensor_entries(parameter_readings, parameter_name):
    if is_sensor_parameter_invalid(parameter_name) or is_sensor_readings_invalid(parameter_readings):
        logger_utility(SENSOR_VALIDATOR_CODES[0])
        return False
    logger_utility(SENSOR_VALIDATOR_CODES[1])
    return True


def logger_utility(log_message):
    print("\n***********SENSOR VALIDATOR LOG START***************")
    print(log_message)
    print("***********SENSOR VALIDATOR LOG END***************")


def print_message_to_console(console_log):
    print(console_log)


