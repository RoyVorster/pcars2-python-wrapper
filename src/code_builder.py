import os
from warnings import filterwarnings, catch_warnings

with catch_warnings():
    filterwarnings('ignore', category=DeprecationWarning)

    # Include local version of pygccxml
    from pygccxml import parser
    from pygccxml import utils

from pyplusplus import module_builder
from pyplusplus.module_builder import call_policies


generator_name, generator_path = 'castxml', 'castxml\\bin\\castxml.exe'

# Find compiler path using cmd 'where'
from subprocess import Popen, PIPE
compiler_name = 'g++'
p = Popen(['where', compiler_name], stdout=PIPE, stderr=PIPE)
compiler_path = p.stdout.read().decode('utf-8').rstrip()

exclude_vars = ['mCarNames', 'mCarClassNames', 'mOrientations', 'mTyreCompound']

class Builder:
    def __init__(self, headers, lib_name, cpp_folder='data_store', result_folder='modules'):        
        self.xml_generator_config = parser.xml_generator_configuration_t(
            xml_generator_path=generator_path,
            xml_generator=generator_name,
            compiler=compiler_name,
            compiler_path=compiler_path
        )

        self.headers = []
        for header in headers:
            self.headers.append(os.path.join(cpp_folder, header))

        self.m_builder = module_builder.module_builder_t(
            self.headers,
            xml_generator_path=generator_path,
            xml_generator_config=self.xml_generator_config
        )

        self.lib_name = lib_name
        self.lib_path = os.path.join(result_folder, self.lib_name) + '.cpp'

        self.filter()

    def build(self):
        self.m_builder.build_code_creator(self.lib_name)

    def write(self):
        self.m_builder.write_module(self.lib_path)

    def filter(self):
        self.m_builder.calldef('get_shared_data').call_policies = call_policies.return_value_policy(call_policies.manage_new_object)
        
        vars_to_exclude = self.m_builder.variables(lambda decl: decl.name in exclude_vars)
        vars_to_exclude.exclude()
