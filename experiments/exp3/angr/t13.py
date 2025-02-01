import time

import angr
import claripy

project = angr.Project('../input/t13', auto_load_libs=False)
func_addr = project.loader.main_object.get_symbol("func")
x = claripy.BVS('x', 32)
y = claripy.BVS('y', 32)
det = claripy.BVS('det', 32)

state = project.factory.call_state(func_addr.rebased_addr, x, y, det)
state.solver.add(x < 100)
state.solver.add(y < 100)

simgr = project.factory.simulation_manager(state)

start = time.time()

cnt = 0
while len(simgr.active) > 0:
    simgr.step()

    if len(simgr.deadended) > 0:
        cnt += len(simgr.deadended)
        simgr.drop(stash="deadended")

end = time.time()
print(f"Total Execution Time: {end - start:.2f} seconds")
print(cnt)
