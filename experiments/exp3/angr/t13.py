import time

import angr
import claripy

project = angr.Project('../input/t13', auto_load_libs=False)
func_addr = project.loader.main_object.get_symbol("func")
x = claripy.BVS('x', 32)
y = claripy.BVS('y', 32)
det = claripy.BVS('det', 32)

state = project.factory.call_state(func_addr.rebased_addr, x, y, det)
state.solver.add(x < 50)
state.solver.add(y < 50)

simgr = project.factory.simulation_manager(state)

start = time.time()

max_paths = 0
max_constraints = 0
try:
    while len(simgr.active) > 0:
        simgr.step()

        active_paths = len(simgr.active)
        if active_paths > max_paths:
            max_paths = active_paths
            constraint_count = sum(len(active.solver.constraints) for active in simgr.active)
            max_constraints = constraint_count
except Exception as e:
    print(max_paths)
    print(max_constraints)

end = time.time()
print(f"Total Execution Time: {end - start:.2f} seconds")
print(f"Max Active Paths: {max_paths}")
print(f"Max Constraint Count: {max_constraints}")
