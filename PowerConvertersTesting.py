from pyfmi import load_fmu
from pymodelica import compile_fmu
from pylab import *

# fmu = compile_fmu("Modelica.Electrical.PowerConverters.Examples.DCAC.MultiPhaseTwoLevel.MultiPhaseTwoLevel_RL")
# fmu = compile_fmu("Modelica.Electrical.PowerConverters.Examples.DCAC.SinglePhaseTwoLevel.SinglePhaseTwoLevel_RL")
# fmu = compile_fmu("Modelica.Electrical.PowerConverters.Examples.DCDC.HBridge.HBridge_DC_Drive")

# fmu = compile_fmu("PowerConvertersTesting.Examples.DCAC.SinglePhaseTwoLevel.SinglePhaseTwoLevel_RL","PowerConvertersTesting.mo")
# fmu = compile_fmu("PowerConvertersTesting.Examples.DCAC.MultiPhaseTwoLevel.MultiPhaseTwoLevel_RL","PowerConvertersTesting.mo")
fmu = compile_fmu("PowerConvertersTesting.Examples.DCDC.HBridge.HBridge_DC_Drive","PowerConvertersTesting.mo")

model = load_fmu(fmu)

opts = model.simulate_options()
opts["ncp"] = 2000
res = model.simulate(final_time=0.1,options=opts)

