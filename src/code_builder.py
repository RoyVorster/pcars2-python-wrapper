import os
from warnings import filterwarnings, catch_warnings

with catch_warnings():
    filterwarnings("ignore",category=DeprecationWarning)
    from pygccxml import parser

from pyplusplus import module_builder
from pyplusplus.module_builder import call_policies

generator_path = "/usr/bin/castxml"
generator_name = "castxml"
compiler = "gnu"
compiler_path = "/usr/bin/g++"

cpp_folder = 'data_store'

exclude_vars = ["mCarNames", "mCarClassNames", "mOrientations", "mTyreCompound"]

class Builder:
    def __init__(self, headers, lib_name):        
        self.xml_generator_config = parser.xml_generator_configuration_t(
            xml_generator_path=generator_path,
            xml_generator=generator_name,
            compiler=compiler,
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
        self.lib_path = os.path.join('module', self.lib_name) + '.cpp'

        self.filter()

    def build(self):
        self.m_builder.build_code_creator(self.lib_name)

    def write(self):
        self.m_builder.write_module(self.lib_path)

    def filter(self):
        self.m_builder.calldef('get_shared_data').call_policies = call_policies.return_value_policy(call_policies.manage_new_object)
        
        vars_to_exclude = self.m_builder.variables(lambda decl: decl.name in exclude_vars)
        vars_to_exclude.exclude()
        
