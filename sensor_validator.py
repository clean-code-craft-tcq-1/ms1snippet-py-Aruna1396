import sensor_IO_handler as handler


def within_tolerance_limit(current_value, next_value, max_delta_value):
    if next_value - current_value > max_delta_value:
        return False
    return True


def is_sensor_reading_without_spikes(parameter_readings, parameter_name):
    last_but_one_reading = len(parameter_readings) - 1
    for i in range(last_but_one_reading):
        if (
                not within_tolerance_limit(parameter_readings[i], parameter_readings[i + 1],
                                           handler.MAX_DELTA_VALUE[parameter_name])):
            handler.logger_utility(handler.SENSOR_VALIDATOR_CODES[3][parameter_name])
            return False
    handler.logger_utility(handler.SENSOR_VALIDATOR_CODES[2][parameter_name])
    return True


def validate_sensor_readings(parameter_readings, parameter_name):
    if handler.validate_input_sensor_entries(parameter_readings, parameter_name):
        return is_sensor_reading_without_spikes(parameter_readings, parameter_name)
    else:
        handler.print_message_to_console('\n ALERT!!! Input Sensor Readings are Invalid. Enter correct values to proceed '
                                                                                 'for validation')
        handler.logger_utility(handler.SENSOR_VALIDATOR_CODES[0])
        return False
