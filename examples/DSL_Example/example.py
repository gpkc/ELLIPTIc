from elliptic.Kernel.DSL import DSL

from src.DSL import VectorTemplateManager, VectorContract, VectorMeta
from src.Expressions import Range


dsl = DSL(VectorTemplateManager(),
          VectorContract(),
          VectorDSL())


with dsl.root() as root:
    ents = root.Range(start=0, count=100)

dsl.get_built_module().get_arr()
