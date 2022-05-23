# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class BillingPlanInformation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'app_store_receipt': 'AppStoreReceipt',
        'billing_address': 'AccountAddress',
        'credit_card_information': 'CreditCardInformation',
        'direct_debit_processor_information': 'DirectDebitProcessorInformation',
        'downgrade_reason': 'str',
        'enable_pre_auth': 'str',
        'enable_support': 'str',
        'included_seats': 'str',
        'incremental_seats': 'str',
        'payment_method': 'str',
        'payment_processor_information': 'PaymentProcessorInformation',
        'plan_information': 'PlanInformation',
        'process_payment': 'str',
        'referral_information': 'ReferralInformation',
        'renewal_status': 'str',
        'sale_discount_amount': 'str',
        'sale_discount_fixed_amount': 'str',
        'sale_discount_percent': 'str',
        'sale_discount_periods': 'str',
        'sale_discount_seat_price_override': 'str',
        'tax_exempt_id': 'str'
    }

    attribute_map = {
        'app_store_receipt': 'appStoreReceipt',
        'billing_address': 'billingAddress',
        'credit_card_information': 'creditCardInformation',
        'direct_debit_processor_information': 'directDebitProcessorInformation',
        'downgrade_reason': 'downgradeReason',
        'enable_pre_auth': 'enablePreAuth',
        'enable_support': 'enableSupport',
        'included_seats': 'includedSeats',
        'incremental_seats': 'incrementalSeats',
        'payment_method': 'paymentMethod',
        'payment_processor_information': 'paymentProcessorInformation',
        'plan_information': 'planInformation',
        'process_payment': 'processPayment',
        'referral_information': 'referralInformation',
        'renewal_status': 'renewalStatus',
        'sale_discount_amount': 'saleDiscountAmount',
        'sale_discount_fixed_amount': 'saleDiscountFixedAmount',
        'sale_discount_percent': 'saleDiscountPercent',
        'sale_discount_periods': 'saleDiscountPeriods',
        'sale_discount_seat_price_override': 'saleDiscountSeatPriceOverride',
        'tax_exempt_id': 'taxExemptId'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BillingPlanInformation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._app_store_receipt = None
        self._billing_address = None
        self._credit_card_information = None
        self._direct_debit_processor_information = None
        self._downgrade_reason = None
        self._enable_pre_auth = None
        self._enable_support = None
        self._included_seats = None
        self._incremental_seats = None
        self._payment_method = None
        self._payment_processor_information = None
        self._plan_information = None
        self._process_payment = None
        self._referral_information = None
        self._renewal_status = None
        self._sale_discount_amount = None
        self._sale_discount_fixed_amount = None
        self._sale_discount_percent = None
        self._sale_discount_periods = None
        self._sale_discount_seat_price_override = None
        self._tax_exempt_id = None
        self.discriminator = None

        setattr(self, "_{}".format('app_store_receipt'), kwargs.get('app_store_receipt', None))
        setattr(self, "_{}".format('billing_address'), kwargs.get('billing_address', None))
        setattr(self, "_{}".format('credit_card_information'), kwargs.get('credit_card_information', None))
        setattr(self, "_{}".format('direct_debit_processor_information'), kwargs.get('direct_debit_processor_information', None))
        setattr(self, "_{}".format('downgrade_reason'), kwargs.get('downgrade_reason', None))
        setattr(self, "_{}".format('enable_pre_auth'), kwargs.get('enable_pre_auth', None))
        setattr(self, "_{}".format('enable_support'), kwargs.get('enable_support', None))
        setattr(self, "_{}".format('included_seats'), kwargs.get('included_seats', None))
        setattr(self, "_{}".format('incremental_seats'), kwargs.get('incremental_seats', None))
        setattr(self, "_{}".format('payment_method'), kwargs.get('payment_method', None))
        setattr(self, "_{}".format('payment_processor_information'), kwargs.get('payment_processor_information', None))
        setattr(self, "_{}".format('plan_information'), kwargs.get('plan_information', None))
        setattr(self, "_{}".format('process_payment'), kwargs.get('process_payment', None))
        setattr(self, "_{}".format('referral_information'), kwargs.get('referral_information', None))
        setattr(self, "_{}".format('renewal_status'), kwargs.get('renewal_status', None))
        setattr(self, "_{}".format('sale_discount_amount'), kwargs.get('sale_discount_amount', None))
        setattr(self, "_{}".format('sale_discount_fixed_amount'), kwargs.get('sale_discount_fixed_amount', None))
        setattr(self, "_{}".format('sale_discount_percent'), kwargs.get('sale_discount_percent', None))
        setattr(self, "_{}".format('sale_discount_periods'), kwargs.get('sale_discount_periods', None))
        setattr(self, "_{}".format('sale_discount_seat_price_override'), kwargs.get('sale_discount_seat_price_override', None))
        setattr(self, "_{}".format('tax_exempt_id'), kwargs.get('tax_exempt_id', None))

    @property
    def app_store_receipt(self):
        """Gets the app_store_receipt of this BillingPlanInformation.  # noqa: E501


        :return: The app_store_receipt of this BillingPlanInformation.  # noqa: E501
        :rtype: AppStoreReceipt
        """
        return self._app_store_receipt

    @app_store_receipt.setter
    def app_store_receipt(self, app_store_receipt):
        """Sets the app_store_receipt of this BillingPlanInformation.


        :param app_store_receipt: The app_store_receipt of this BillingPlanInformation.  # noqa: E501
        :type: AppStoreReceipt
        """

        self._app_store_receipt = app_store_receipt

    @property
    def billing_address(self):
        """Gets the billing_address of this BillingPlanInformation.  # noqa: E501


        :return: The billing_address of this BillingPlanInformation.  # noqa: E501
        :rtype: AccountAddress
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this BillingPlanInformation.


        :param billing_address: The billing_address of this BillingPlanInformation.  # noqa: E501
        :type: AccountAddress
        """

        self._billing_address = billing_address

    @property
    def credit_card_information(self):
        """Gets the credit_card_information of this BillingPlanInformation.  # noqa: E501


        :return: The credit_card_information of this BillingPlanInformation.  # noqa: E501
        :rtype: CreditCardInformation
        """
        return self._credit_card_information

    @credit_card_information.setter
    def credit_card_information(self, credit_card_information):
        """Sets the credit_card_information of this BillingPlanInformation.


        :param credit_card_information: The credit_card_information of this BillingPlanInformation.  # noqa: E501
        :type: CreditCardInformation
        """

        self._credit_card_information = credit_card_information

    @property
    def direct_debit_processor_information(self):
        """Gets the direct_debit_processor_information of this BillingPlanInformation.  # noqa: E501


        :return: The direct_debit_processor_information of this BillingPlanInformation.  # noqa: E501
        :rtype: DirectDebitProcessorInformation
        """
        return self._direct_debit_processor_information

    @direct_debit_processor_information.setter
    def direct_debit_processor_information(self, direct_debit_processor_information):
        """Sets the direct_debit_processor_information of this BillingPlanInformation.


        :param direct_debit_processor_information: The direct_debit_processor_information of this BillingPlanInformation.  # noqa: E501
        :type: DirectDebitProcessorInformation
        """

        self._direct_debit_processor_information = direct_debit_processor_information

    @property
    def downgrade_reason(self):
        """Gets the downgrade_reason of this BillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The downgrade_reason of this BillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._downgrade_reason

    @downgrade_reason.setter
    def downgrade_reason(self, downgrade_reason):
        """Sets the downgrade_reason of this BillingPlanInformation.

          # noqa: E501

        :param downgrade_reason: The downgrade_reason of this BillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._downgrade_reason = downgrade_reason

    @property
    def enable_pre_auth(self):
        """Gets the enable_pre_auth of this BillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The enable_pre_auth of this BillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._enable_pre_auth

    @enable_pre_auth.setter
    def enable_pre_auth(self, enable_pre_auth):
        """Sets the enable_pre_auth of this BillingPlanInformation.

          # noqa: E501

        :param enable_pre_auth: The enable_pre_auth of this BillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._enable_pre_auth = enable_pre_auth

    @property
    def enable_support(self):
        """Gets the enable_support of this BillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The enable_support of this BillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._enable_support

    @enable_support.setter
    def enable_support(self, enable_support):
        """Sets the enable_support of this BillingPlanInformation.

          # noqa: E501

        :param enable_support: The enable_support of this BillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._enable_support = enable_support

    @property
    def included_seats(self):
        """Gets the included_seats of this BillingPlanInformation.  # noqa: E501

        The number of seats (users) included.  # noqa: E501

        :return: The included_seats of this BillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._included_seats

    @included_seats.setter
    def included_seats(self, included_seats):
        """Sets the included_seats of this BillingPlanInformation.

        The number of seats (users) included.  # noqa: E501

        :param included_seats: The included_seats of this BillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._included_seats = included_seats

    @property
    def incremental_seats(self):
        """Gets the incremental_seats of this BillingPlanInformation.  # noqa: E501

        Reserved: TBD  # noqa: E501

        :return: The incremental_seats of this BillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._incremental_seats

    @incremental_seats.setter
    def incremental_seats(self, incremental_seats):
        """Sets the incremental_seats of this BillingPlanInformation.

        Reserved: TBD  # noqa: E501

        :param incremental_seats: The incremental_seats of this BillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._incremental_seats = incremental_seats

    @property
    def payment_method(self):
        """Gets the payment_method of this BillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The payment_method of this BillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this BillingPlanInformation.

          # noqa: E501

        :param payment_method: The payment_method of this BillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def payment_processor_information(self):
        """Gets the payment_processor_information of this BillingPlanInformation.  # noqa: E501


        :return: The payment_processor_information of this BillingPlanInformation.  # noqa: E501
        :rtype: PaymentProcessorInformation
        """
        return self._payment_processor_information

    @payment_processor_information.setter
    def payment_processor_information(self, payment_processor_information):
        """Sets the payment_processor_information of this BillingPlanInformation.


        :param payment_processor_information: The payment_processor_information of this BillingPlanInformation.  # noqa: E501
        :type: PaymentProcessorInformation
        """

        self._payment_processor_information = payment_processor_information

    @property
    def plan_information(self):
        """Gets the plan_information of this BillingPlanInformation.  # noqa: E501


        :return: The plan_information of this BillingPlanInformation.  # noqa: E501
        :rtype: PlanInformation
        """
        return self._plan_information

    @plan_information.setter
    def plan_information(self, plan_information):
        """Sets the plan_information of this BillingPlanInformation.


        :param plan_information: The plan_information of this BillingPlanInformation.  # noqa: E501
        :type: PlanInformation
        """

        self._plan_information = plan_information

    @property
    def process_payment(self):
        """Gets the process_payment of this BillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The process_payment of this BillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._process_payment

    @process_payment.setter
    def process_payment(self, process_payment):
        """Sets the process_payment of this BillingPlanInformation.

          # noqa: E501

        :param process_payment: The process_payment of this BillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._process_payment = process_payment

    @property
    def referral_information(self):
        """Gets the referral_information of this BillingPlanInformation.  # noqa: E501


        :return: The referral_information of this BillingPlanInformation.  # noqa: E501
        :rtype: ReferralInformation
        """
        return self._referral_information

    @referral_information.setter
    def referral_information(self, referral_information):
        """Sets the referral_information of this BillingPlanInformation.


        :param referral_information: The referral_information of this BillingPlanInformation.  # noqa: E501
        :type: ReferralInformation
        """

        self._referral_information = referral_information

    @property
    def renewal_status(self):
        """Gets the renewal_status of this BillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The renewal_status of this BillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._renewal_status

    @renewal_status.setter
    def renewal_status(self, renewal_status):
        """Sets the renewal_status of this BillingPlanInformation.

          # noqa: E501

        :param renewal_status: The renewal_status of this BillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._renewal_status = renewal_status

    @property
    def sale_discount_amount(self):
        """Gets the sale_discount_amount of this BillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The sale_discount_amount of this BillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._sale_discount_amount

    @sale_discount_amount.setter
    def sale_discount_amount(self, sale_discount_amount):
        """Sets the sale_discount_amount of this BillingPlanInformation.

          # noqa: E501

        :param sale_discount_amount: The sale_discount_amount of this BillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._sale_discount_amount = sale_discount_amount

    @property
    def sale_discount_fixed_amount(self):
        """Gets the sale_discount_fixed_amount of this BillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The sale_discount_fixed_amount of this BillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._sale_discount_fixed_amount

    @sale_discount_fixed_amount.setter
    def sale_discount_fixed_amount(self, sale_discount_fixed_amount):
        """Sets the sale_discount_fixed_amount of this BillingPlanInformation.

          # noqa: E501

        :param sale_discount_fixed_amount: The sale_discount_fixed_amount of this BillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._sale_discount_fixed_amount = sale_discount_fixed_amount

    @property
    def sale_discount_percent(self):
        """Gets the sale_discount_percent of this BillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The sale_discount_percent of this BillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._sale_discount_percent

    @sale_discount_percent.setter
    def sale_discount_percent(self, sale_discount_percent):
        """Sets the sale_discount_percent of this BillingPlanInformation.

          # noqa: E501

        :param sale_discount_percent: The sale_discount_percent of this BillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._sale_discount_percent = sale_discount_percent

    @property
    def sale_discount_periods(self):
        """Gets the sale_discount_periods of this BillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The sale_discount_periods of this BillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._sale_discount_periods

    @sale_discount_periods.setter
    def sale_discount_periods(self, sale_discount_periods):
        """Sets the sale_discount_periods of this BillingPlanInformation.

          # noqa: E501

        :param sale_discount_periods: The sale_discount_periods of this BillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._sale_discount_periods = sale_discount_periods

    @property
    def sale_discount_seat_price_override(self):
        """Gets the sale_discount_seat_price_override of this BillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The sale_discount_seat_price_override of this BillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._sale_discount_seat_price_override

    @sale_discount_seat_price_override.setter
    def sale_discount_seat_price_override(self, sale_discount_seat_price_override):
        """Sets the sale_discount_seat_price_override of this BillingPlanInformation.

          # noqa: E501

        :param sale_discount_seat_price_override: The sale_discount_seat_price_override of this BillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._sale_discount_seat_price_override = sale_discount_seat_price_override

    @property
    def tax_exempt_id(self):
        """Gets the tax_exempt_id of this BillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The tax_exempt_id of this BillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._tax_exempt_id

    @tax_exempt_id.setter
    def tax_exempt_id(self, tax_exempt_id):
        """Sets the tax_exempt_id of this BillingPlanInformation.

          # noqa: E501

        :param tax_exempt_id: The tax_exempt_id of this BillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._tax_exempt_id = tax_exempt_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BillingPlanInformation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BillingPlanInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BillingPlanInformation):
            return True

        return self.to_dict() != other.to_dict()
