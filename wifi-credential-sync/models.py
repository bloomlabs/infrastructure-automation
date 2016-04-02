# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Float, Index, Integer, Numeric, String, Table, text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class BatchHistory(Base):
    __tablename__ = 'batch_history'

    id = Column(Integer, primary_key=True)
    batch_name = Column(String(64), index=True)
    batch_description = Column(String(256))
    hotspot_id = Column(Integer, server_default=text("'0'"))
    batch_status = Column(String(128), nullable=False, server_default=text("'Pending'"))
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))


class BillingHistory(Base):
    __tablename__ = 'billing_history'

    id = Column(Integer, primary_key=True)
    username = Column(String(128), index=True)
    planId = Column(Integer)
    billAmount = Column(String(200))
    billAction = Column(String(128), nullable=False, server_default=text("'Unavailable'"))
    billPerformer = Column(String(200))
    billReason = Column(String(200))
    paymentmethod = Column(String(200))
    cash = Column(String(200))
    creditcardname = Column(String(200))
    creditcardnumber = Column(String(200))
    creditcardverification = Column(String(200))
    creditcardtype = Column(String(200))
    creditcardexp = Column(String(200))
    coupon = Column(String(200))
    discount = Column(String(200))
    notes = Column(String(200))
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))


class BillingMerchant(Base):
    __tablename__ = 'billing_merchant'

    id = Column(Integer, primary_key=True)
    username = Column(String(128), nullable=False, index=True, server_default=text("''"))
    password = Column(String(128), nullable=False, server_default=text("''"))
    mac = Column(String(200), nullable=False, server_default=text("''"))
    pin = Column(String(200), nullable=False, server_default=text("''"))
    txnId = Column(String(200), nullable=False, server_default=text("''"))
    planName = Column(String(128), nullable=False, server_default=text("''"))
    planId = Column(Integer, nullable=False)
    quantity = Column(String(200), nullable=False, server_default=text("''"))
    business_email = Column(String(200), nullable=False, server_default=text("''"))
    business_id = Column(String(200), nullable=False, server_default=text("''"))
    txn_type = Column(String(200), nullable=False, server_default=text("''"))
    txn_id = Column(String(200), nullable=False, server_default=text("''"))
    payment_type = Column(String(200), nullable=False, server_default=text("''"))
    payment_tax = Column(String(200), nullable=False, server_default=text("''"))
    payment_cost = Column(String(200), nullable=False, server_default=text("''"))
    payment_fee = Column(String(200), nullable=False, server_default=text("''"))
    payment_total = Column(String(200), nullable=False, server_default=text("''"))
    payment_currency = Column(String(200), nullable=False, server_default=text("''"))
    first_name = Column(String(200), nullable=False, server_default=text("''"))
    last_name = Column(String(200), nullable=False, server_default=text("''"))
    payer_email = Column(String(200), nullable=False, server_default=text("''"))
    payer_address_name = Column(String(200), nullable=False, server_default=text("''"))
    payer_address_street = Column(String(200), nullable=False, server_default=text("''"))
    payer_address_country = Column(String(200), nullable=False, server_default=text("''"))
    payer_address_country_code = Column(String(200), nullable=False, server_default=text("''"))
    payer_address_city = Column(String(200), nullable=False, server_default=text("''"))
    payer_address_state = Column(String(200), nullable=False, server_default=text("''"))
    payer_address_zip = Column(String(200), nullable=False, server_default=text("''"))
    payment_date = Column(DateTime, nullable=False)
    payment_status = Column(String(200), nullable=False, server_default=text("''"))
    pending_reason = Column(String(200), nullable=False, server_default=text("''"))
    reason_code = Column(String(200), nullable=False, server_default=text("''"))
    receipt_ID = Column(String(200), nullable=False, server_default=text("''"))
    payment_address_status = Column(String(200), nullable=False, server_default=text("''"))
    vendor_type = Column(String(200), nullable=False, server_default=text("''"))
    payer_status = Column(String(200), nullable=False, server_default=text("''"))


class BillingPaypal(Base):
    __tablename__ = 'billing_paypal'

    id = Column(Integer, primary_key=True)
    username = Column(String(128), index=True)
    password = Column(String(128))
    mac = Column(String(200))
    pin = Column(String(200))
    txnId = Column(String(200))
    planName = Column(String(128))
    planId = Column(String(200))
    quantity = Column(String(200))
    receiver_email = Column(String(200))
    business = Column(String(200))
    tax = Column(String(200))
    mc_gross = Column(String(200))
    mc_fee = Column(String(200))
    mc_currency = Column(String(200))
    first_name = Column(String(200))
    last_name = Column(String(200))
    payer_email = Column(String(200))
    address_name = Column(String(200))
    address_street = Column(String(200))
    address_country = Column(String(200))
    address_country_code = Column(String(200))
    address_city = Column(String(200))
    address_state = Column(String(200))
    address_zip = Column(String(200))
    payment_date = Column(DateTime)
    payment_status = Column(String(200))
    payment_address_status = Column(String(200))
    payer_status = Column(String(200))


class BillingPlan(Base):
    __tablename__ = 'billing_plans'

    id = Column(Integer, primary_key=True)
    planName = Column(String(128), index=True)
    planId = Column(String(128))
    planType = Column(String(128))
    planTimeBank = Column(String(128))
    planTimeType = Column(String(128))
    planTimeRefillCost = Column(String(128))
    planBandwidthUp = Column(String(128))
    planBandwidthDown = Column(String(128))
    planTrafficTotal = Column(String(128))
    planTrafficUp = Column(String(128))
    planTrafficDown = Column(String(128))
    planTrafficRefillCost = Column(String(128))
    planRecurring = Column(String(128))
    planRecurringPeriod = Column(String(128))
    planRecurringBillingSchedule = Column(String(128), nullable=False, server_default=text("'Fixed'"))
    planCost = Column(String(128))
    planSetupCost = Column(String(128))
    planTax = Column(String(128))
    planCurrency = Column(String(128))
    planGroup = Column(String(128))
    planActive = Column(String(32), nullable=False, server_default=text("'yes'"))
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))


class BillingPlansProfile(Base):
    __tablename__ = 'billing_plans_profiles'

    id = Column(Integer, primary_key=True)
    plan_name = Column(String(128), nullable=False)
    profile_name = Column(String(256))


class BillingRate(Base):
    __tablename__ = 'billing_rates'

    id = Column(Integer, primary_key=True)
    rateName = Column(String(128), nullable=False, index=True, server_default=text("''"))
    rateType = Column(String(128), nullable=False, server_default=text("''"))
    rateCost = Column(Integer, nullable=False, server_default=text("'0'"))
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))


class CUI(Base):
    __tablename__ = 'cui'

    clientipaddress = Column(String(15), primary_key=True, nullable=False, server_default=text("''"))
    callingstationid = Column(String(50), primary_key=True, nullable=False, server_default=text("''"))
    username = Column(String(64), primary_key=True, nullable=False, server_default=text("''"))
    cui = Column(String(32), nullable=False, server_default=text("''"))
    creationdate = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    lastaccounting = Column(DateTime, nullable=False)


class Dictionary(Base):
    __tablename__ = 'dictionary'

    id = Column(Integer, primary_key=True)
    Type = Column(String(30))
    Attribute = Column(String(64))
    Value = Column(String(64))
    Format = Column(String(20))
    Vendor = Column(String(32))
    RecommendedOP = Column(String(32))
    RecommendedTable = Column(String(32))
    RecommendedHelper = Column(String(32))
    RecommendedTooltip = Column(String(512))


class Hotspot(Base):
    __tablename__ = 'hotspots'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(200), index=True)
    mac = Column(String(200), index=True)
    geocode = Column(String(200))
    owner = Column(String(200))
    email_owner = Column(String(200))
    manager = Column(String(200))
    email_manager = Column(String(200))
    address = Column(String(200))
    company = Column(String(200))
    phone1 = Column(String(200))
    phone2 = Column(String(200))
    type = Column(String(200))
    companywebsite = Column(String(200))
    companyemail = Column(String(200))
    companycontact = Column(String(200))
    companyphone = Column(String(200))
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))


class Invoice(Base):
    __tablename__ = 'invoice'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    batch_id = Column(Integer)
    date = Column(DateTime, nullable=False)
    status_id = Column(Integer, nullable=False, server_default=text("'1'"))
    type_id = Column(Integer, nullable=False, server_default=text("'1'"))
    notes = Column(String(128), nullable=False)
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))


class InvoiceItem(Base):
    __tablename__ = 'invoice_items'

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, nullable=False)
    plan_id = Column(Integer)
    amount = Column(Numeric(10, 2), nullable=False, server_default=text("'0.00'"))
    tax_amount = Column(Numeric(10, 2), nullable=False, server_default=text("'0.00'"))
    total = Column(Numeric(10, 2), nullable=False, server_default=text("'0.00'"))
    notes = Column(String(128), nullable=False)
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))


class InvoiceStatu(Base):
    __tablename__ = 'invoice_status'

    id = Column(Integer, primary_key=True)
    value = Column(String(32), nullable=False, server_default=text("''"))
    notes = Column(String(128), nullable=False)
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))


class InvoiceType(Base):
    __tablename__ = 'invoice_type'

    id = Column(Integer, primary_key=True)
    value = Column(String(32), nullable=False, server_default=text("''"))
    notes = Column(String(128), nullable=False)
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))


class NAS(Base):
    __tablename__ = 'nas'

    id = Column(Integer, primary_key=True)
    nasname = Column(String(128, u'utf8_unicode_ci'), nullable=False, index=True)
    shortname = Column(String(32, u'utf8_unicode_ci'))
    type = Column(String(30, u'utf8_unicode_ci'), server_default=text("'other'"))
    ports = Column(Integer)
    secret = Column(String(60, u'utf8_unicode_ci'), nullable=False, server_default=text("'secret'"))
    server = Column(String(64, u'utf8_unicode_ci'))
    community = Column(String(50, u'utf8_unicode_ci'))
    description = Column(String(200, u'utf8_unicode_ci'), server_default=text("'RADIUS Client'"))


class Node(Base):
    __tablename__ = 'node'

    id = Column(Integer, primary_key=True)
    time = Column(DateTime, nullable=False)
    netid = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    latitude = Column(String(20), nullable=False)
    longitude = Column(String(20), nullable=False)
    owner_name = Column(String(50), nullable=False)
    owner_email = Column(String(50), nullable=False)
    owner_phone = Column(String(25), nullable=False)
    owner_address = Column(String(100), nullable=False)
    approval_status = Column(String(1), nullable=False)
    ip = Column(String(20), nullable=False)
    mac = Column(String(20), nullable=False, unique=True)
    uptime = Column(String(100), nullable=False)
    robin = Column(String(20), nullable=False)
    batman = Column(String(20), nullable=False)
    memfree = Column(String(20), nullable=False)
    nbs = Column(String, nullable=False)
    gateway = Column(String(20), nullable=False)
    gw_qual = Column('gw-qual', String(20), nullable=False)
    routes = Column(String, nullable=False)
    users = Column(String(3), nullable=False)
    kbdown = Column(String(20), nullable=False)
    kbup = Column(String(20), nullable=False)
    hops = Column(String(3), nullable=False)
    rank = Column(String(3), nullable=False)
    ssid = Column(String(20), nullable=False)
    pssid = Column(String(20), nullable=False)
    gateway_bit = Column(Integer, nullable=False)
    memlow = Column(String(20), nullable=False)
    usershi = Column(String(3), nullable=False)
    cpu = Column(Float, nullable=False, server_default=text("'0'"))
    wan_iface = Column(String(128))
    wan_ip = Column(String(128))
    wan_mac = Column(String(128))
    wan_gateway = Column(String(128))
    wifi_iface = Column(String(128))
    wifi_ip = Column(String(128))
    wifi_mac = Column(String(128))
    wifi_ssid = Column(String(128))
    wifi_key = Column(String(128))
    wifi_channel = Column(String(128))
    lan_iface = Column(String(128))
    lan_mac = Column(String(128))
    lan_ip = Column(String(128))
    wan_bup = Column(String(128))
    wan_bdown = Column(String(128))
    firmware = Column(String(128))
    firmware_revision = Column(String(128))


class Operator(Base):
    __tablename__ = 'operators'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, index=True)
    password = Column(String(32), nullable=False)
    firstname = Column(String(32), nullable=False)
    lastname = Column(String(32), nullable=False)
    title = Column(String(32), nullable=False)
    department = Column(String(32), nullable=False)
    company = Column(String(32), nullable=False)
    phone1 = Column(String(32), nullable=False)
    phone2 = Column(String(32), nullable=False)
    email1 = Column(String(32), nullable=False)
    email2 = Column(String(32), nullable=False)
    messenger1 = Column(String(32), nullable=False)
    messenger2 = Column(String(32), nullable=False)
    notes = Column(String(128), nullable=False)
    lastlogin = Column(DateTime)
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))


class OperatorACL(Base):
    __tablename__ = 'operators_acl'

    id = Column(Integer, primary_key=True)
    operator_id = Column(Integer, nullable=False)
    file = Column(String(128), nullable=False)
    access = Column(Integer, nullable=False, server_default=text("'0'"))


class OperatorACLFIle(Base):
    __tablename__ = 'operators_acl_files'

    id = Column(Integer, primary_key=True)
    file = Column(String(128), nullable=False)
    category = Column(String(128), nullable=False)
    section = Column(String(128), nullable=False)


class Payment(Base):
    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    date = Column(DateTime, nullable=False)
    type_id = Column(Integer, nullable=False, server_default=text("'1'"))
    notes = Column(String(128), nullable=False)
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))


class PaymentType(Base):
    __tablename__ = 'payment_type'

    id = Column(Integer, primary_key=True)
    value = Column(String(32), nullable=False, server_default=text("''"))
    notes = Column(String(128), nullable=False)
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))


class Proxy(Base):
    __tablename__ = 'proxys'

    id = Column(BigInteger, primary_key=True)
    proxyname = Column(String(128))
    retry_delay = Column(Integer)
    retry_count = Column(Integer)
    dead_time = Column(Integer)
    default_fallback = Column(Integer)
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))


class RADAcct(Base):
    __tablename__ = 'radacct'

    radacctid = Column(BigInteger, primary_key=True)
    acctsessionid = Column(String(64, u'utf8_unicode_ci'), nullable=False, index=True, server_default=text("''"))
    acctuniqueid = Column(String(32, u'utf8_unicode_ci'), nullable=False, index=True, server_default=text("''"))
    username = Column(String(64, u'utf8_unicode_ci'), ForeignKey('userinfo.username'), nullable=False, index=True, server_default=text("''"))
    user = relationship("UserInfo", back_populates="radaccts")

    groupname = Column(String(64, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))
    realm = Column(String(64, u'utf8_unicode_ci'), server_default=text("''"))
    nasipaddress = Column(String(15, u'utf8_unicode_ci'), nullable=False, index=True, server_default=text("''"))
    nasportid = Column(String(15, u'utf8_unicode_ci'))
    nasporttype = Column(String(32, u'utf8_unicode_ci'))
    acctstarttime = Column(DateTime, index=True)
    acctstoptime = Column(DateTime, index=True)
    acctsessiontime = Column(Integer, index=True)
    acctauthentic = Column(String(32, u'utf8_unicode_ci'))
    connectinfo_start = Column(String(50, u'utf8_unicode_ci'))
    connectinfo_stop = Column(String(50, u'utf8_unicode_ci'))
    acctinputoctets = Column(BigInteger)
    acctoutputoctets = Column(BigInteger)
    calledstationid = Column(String(50, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))
    callingstationid = Column(String(50, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))
    acctterminatecause = Column(String(32, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))
    servicetype = Column(String(32, u'utf8_unicode_ci'))
    framedprotocol = Column(String(32, u'utf8_unicode_ci'))
    framedipaddress = Column(String(15, u'utf8_unicode_ci'), nullable=False, index=True, server_default=text("''"))
    acctstartdelay = Column(Integer)
    acctstopdelay = Column(Integer)
    xascendsessionsvrkey = Column(String(10, u'utf8_unicode_ci'))


class RADCheck(Base):
    __tablename__ = 'radcheck'

    id = Column(Integer, primary_key=True)
    username = Column(String(64, u'utf8_unicode_ci'), ForeignKey('userinfo.username'), nullable=False, index=True, server_default=text("''"))
    user = relationship("UserInfo", back_populates="radchecks")

    attribute = Column(String(64, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))
    op = Column(String(2, u'utf8_unicode_ci'), nullable=False, server_default=text("'=='"))
    value = Column(String(253, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))

    def __repr__(self):
        return "<RADCheck('{}', '{}' {} '{}')>".format(self.username, self.attribute, self.op, self.value)


class RADGroupCheck(Base):
    __tablename__ = 'radgroupcheck'

    id = Column(Integer, primary_key=True)
    groupname = Column(String(64, u'utf8_unicode_ci'), nullable=False, index=True, server_default=text("''"))
    attribute = Column(String(64, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))
    op = Column(String(2, u'utf8_unicode_ci'), nullable=False, server_default=text("'=='"))
    value = Column(String(253, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))


class RADGroupReply(Base):
    __tablename__ = 'radgroupreply'

    id = Column(Integer, primary_key=True)
    groupname = Column(String(64, u'utf8_unicode_ci'), nullable=False, index=True, server_default=text("''"))
    attribute = Column(String(64, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))
    op = Column(String(2, u'utf8_unicode_ci'), nullable=False, server_default=text("'='"))
    value = Column(String(253, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))


class RADHuntGroup(Base):
    __tablename__ = 'radhuntgroup'

    id = Column(Integer, primary_key=True)
    groupname = Column(String(64), nullable=False, server_default=text("''"))
    nasipaddress = Column(String(15), nullable=False, index=True, server_default=text("''"))
    nasportid = Column(String(15))


class RADIPPool(Base):
    __tablename__ = 'radippool'
    __table_args__ = (
        Index('radippool_poolname_expire', 'pool_name', 'expiry_time'),
        Index('radippool_nasip_poolkey_ipaddress', 'nasipaddress', 'pool_key', 'framedipaddress')
    )

    id = Column(Integer, primary_key=True)
    pool_name = Column(String(30, u'utf8_unicode_ci'), nullable=False)
    framedipaddress = Column(String(15, u'utf8_unicode_ci'), nullable=False, index=True, server_default=text("''"))
    nasipaddress = Column(String(15, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))
    calledstationid = Column(String(30, u'utf8_unicode_ci'), nullable=False)
    callingstationid = Column(String(30, u'utf8_unicode_ci'), nullable=False)
    expiry_time = Column(DateTime)
    username = Column(String(64, u'utf8_unicode_ci'), ForeignKey('userinfo.username'), nullable=False, server_default=text("''"))
    user = relationship("UserInfo", back_populates="radippools")
    pool_key = Column(String(30, u'utf8_unicode_ci'), nullable=False)


class RADPostAuth(Base):
    __tablename__ = 'radpostauth'

    id = Column(Integer, primary_key=True)
    username = Column(String(64, u'utf8_unicode_ci'), ForeignKey('userinfo.username'), nullable=False, server_default=text("''"))
    user = relationship("UserInfo", back_populates="radpostauths")
    _pass = Column('pass', String(64, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))
    reply = Column(String(32, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))
    authdate = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class RADReply(Base):
    __tablename__ = 'radreply'

    id = Column(Integer, primary_key=True)
    username = Column(String(64, u'utf8_unicode_ci'), ForeignKey('userinfo.username'), nullable=False, index=True, server_default=text("''"))
    user = relationship("UserInfo", back_populates="radreplies")
    attribute = Column(String(64, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))
    op = Column(String(2, u'utf8_unicode_ci'), nullable=False, server_default=text("'='"))
    value = Column(String(253, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))


t_radusergroup = Table(
    'radusergroup', metadata,
    Column('username', String(64, u'utf8_unicode_ci'), nullable=False, index=True, server_default=text("''")),
    Column('groupname', String(64, u'utf8_unicode_ci'), nullable=False, server_default=text("''")),
    Column('priority', Integer, nullable=False, server_default=text("'1'"))
)


class Realm(Base):
    __tablename__ = 'realms'

    id = Column(BigInteger, primary_key=True)
    realmname = Column(String(128))
    type = Column(String(32))
    authhost = Column(String(256))
    accthost = Column(String(256))
    secret = Column(String(128))
    ldflag = Column(String(64))
    nostrip = Column(Integer)
    hints = Column(Integer)
    notrealm = Column(Integer)
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))


class UserBillInfo(Base):
    __tablename__ = 'userbillinfo'

    id = Column(Integer, primary_key=True)
    username = Column(String(128), index=True)
    planName = Column(String(128), index=True)
    hotspot_id = Column(Integer)
    hotspotlocation = Column(String(32))
    contactperson = Column(String(200))
    company = Column(String(200))
    email = Column(String(200))
    phone = Column(String(200))
    address = Column(String(200))
    city = Column(String(200))
    state = Column(String(200))
    country = Column(String(100))
    zip = Column(String(200))
    paymentmethod = Column(String(200))
    cash = Column(String(200))
    creditcardname = Column(String(200))
    creditcardnumber = Column(String(200))
    creditcardverification = Column(String(200))
    creditcardtype = Column(String(200))
    creditcardexp = Column(String(200))
    notes = Column(String(200))
    changeuserbillinfo = Column(String(128))
    lead = Column(String(200))
    coupon = Column(String(200))
    ordertaker = Column(String(200))
    billstatus = Column(String(200))
    lastbill = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    nextbill = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    nextinvoicedue = Column(Integer)
    billdue = Column(Integer)
    postalinvoice = Column(String(8))
    faxinvoice = Column(String(8))
    emailinvoice = Column(String(8))
    batch_id = Column(Integer)
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))


class UserInfo(Base):
    __tablename__ = 'userinfo'

    id = Column(Integer, primary_key=True)
    username = Column(String(128), index=True)
    firstname = Column(String(200))
    lastname = Column(String(200))
    email = Column(String(200))
    department = Column(String(200))
    company = Column(String(200))
    workphone = Column(String(200))
    homephone = Column(String(200))
    mobilephone = Column(String(200))
    address = Column(String(200))
    city = Column(String(200))
    state = Column(String(200))
    country = Column(String(100))
    zip = Column(String(200))
    notes = Column(String(200))
    changeuserinfo = Column(String(128))
    portalloginpassword = Column(String(128), server_default=text("''"))
    enableportallogin = Column(Integer, server_default=text("'0'"))
    creationdate = Column(DateTime)
    creationby = Column(String(128))
    updatedate = Column(DateTime)
    updateby = Column(String(128))

    radchecks = relationship("RADCheck", back_populates="user")
    radreplies = relationship("RADReply", back_populates="user")
    radaccts = relationship("RADAcct", back_populates="user")
    wimaxes = relationship("WiMAX", back_populates="user")
    radippools = relationship("RADIPPool", back_populates="user")
    radpostauths = relationship("RADPostAuth", back_populates="user")

    def __repr__(self):
        return "<UserInfo(username='{}', firstname='{}', lastname='{}')>".format(self.username, self.firstname, self.lastname)


class WiMAX(Base):
    __tablename__ = 'wimax'

    id = Column(Integer, primary_key=True)
    username = Column(String(64, u'utf8_unicode_ci'), ForeignKey('userinfo.username'), nullable=False, index=True, server_default=text("''"))
    user = relationship("UserInfo", back_populates="wimaxes")
    authdate = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    spi = Column(String(16, u'utf8_unicode_ci'), nullable=False, index=True, server_default=text("''"))
    mipkey = Column(String(400, u'utf8_unicode_ci'), nullable=False, server_default=text("''"))
    lifetime = Column(Integer)
