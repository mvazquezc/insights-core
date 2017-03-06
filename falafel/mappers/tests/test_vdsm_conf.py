from falafel.mappers.vdsm_conf import VDSMConf, VDSMConfIni
from falafel.tests import context_wrap


CONF = """
[vars]
ssl = true
cpu_affinity = 1

[addresses]
management_port = 54321
qq = 345
"""


def test_vdsm_conf():
    result = VDSMConf(context_wrap(CONF))
    expected = {'vars': {'ssl': 'true', 'cpu_affinity': '1'}, 'addresses': {'management_port': '54321', 'qq': '345'}}
    assert result.data == expected


def test_vdsm_conf_ini():
    result = VDSMConfIni(context_wrap(CONF))
    assert sorted(result.sections()) == sorted(['vars', 'addresses'])
    assert result.has_option('vars', 'ssl')
    assert result.getboolean('vars', 'ssl')
    assert result.getint('vars', 'cpu_affinity') == 1
    assert result.getint('addresses', 'management_port') == 54321
    assert result.getint('addresses', 'qq') == 345
