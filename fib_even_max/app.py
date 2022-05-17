import logging
import json
from timeit import default_timer as timer
from datetime import timedelta

logger = logging.getLogger(__name__)

"""
A module to find the sum of all even numbers in a fib series
and calculate the performance of different approaches
"""


class FibSum:
    """
    Find the sum of all even numbers in a fib series
    in different ways
    """

    series_max = None

    def __init__(self, max_num):
        self.series_max = max_num

    def __eq__(self, other):
        return isinstance(other, FibSum) and self.series_max == other.series_max

    def __repr__(self):
        return str(vars(self))

    def calculate(self):
        """
        find the sum of all the even numbers up to the limit
        1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
        """
        num1 = 0
        num2 = 1
        sum = 0

        start = timer()

        while(num2 < self.series_max):
            '''
            Using single line multi assignment in python
            This helps with avoiding temporary variable
            as shown below.
            temp = num1
            num1 = num2
            num2 = temp + num2
            '''
            num1, num2 = num2, num1 + num2

            if ((num2 & 0x01) == 0x0):
                sum += num2
        end = timer()

        proc_time = (timedelta(seconds=end-start))

        return(sum, proc_time)

    def calculate_with_temp(self):
        """
        Find the sum of all even numbers in a fib series
        Use a temp variable to hold the previous number
        while calculating the sum
        """
        num1 = 0
        num2 = 1
        sum = 0

        start = timer()

        while(num2 < self.series_max):
            temp = num1
            num1 = num2
            num2 = temp + num2

            if ((num2 & 0x01) == 0x0):
                sum += num2

        end = timer()

        proc_time = (timedelta(seconds=end-start))

        return(sum, proc_time)

    def calculate_with_mod(self):
        """
        Find the sum of all even numbers in a fib series
        Use modulus to check the number is even or odd
        """
        num1 = 0
        num2 = 1
        sum = 0

        start = timer()

        while(num2 < self.series_max):
            '''
            Using single line multi assignment in python
            This helps with avoiding temporary variable
            as shown below.
            temp = num1
            num1 = num2
            num2 = temp + num2
            '''
            num1, num2 = num2, num1 + num2

            if ((num2 % 2) == 0x0):
                sum += num2

        end = timer()

        proc_time = (timedelta(seconds=end-start))

        return(sum, proc_time)


def lambda_handler(event, context):
    """
    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    request = json.loads(event['body'])
    max_series = request['max_series']
    fib_sum = FibSum(max_series)
    # priming...
    series_sum, elapsed_time = fib_sum.calculate()

    series_sum, elapsed_time = fib_sum.calculate()
    print(elapsed_time)
    series_sum_temp, elapsed_time_temp = fib_sum.calculate_with_temp()
    print(elapsed_time_temp)
    series_sum_mod, elapsed_time_mod = fib_sum.calculate_with_mod()
    print(elapsed_time_mod)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "sum_even": {"sum": series_sum, "elapsed_time": str(elapsed_time)},
                "sum_even_temp": {"sum": series_sum_temp, "elapsed_time": str(elapsed_time_temp)},
                "sum_even_mod": {"sum": series_sum_mod, "elapsed_time": str(elapsed_time_mod)},
            }
        ),
    }


def main():
    fib_sum = FibSum(5)
    series_sum, elapsed_time = fib_sum.calculate()
    print(elapsed_time)
    series_sum_temp, elapsed_time_temp = fib_sum.calculate_with_temp()
    print(elapsed_time_temp)
    series_sum_mod, elapsed_time_mod = fib_sum.calculate_with_mod()
    print(elapsed_time_mod)


if __name__ == '__main__':
    main()
