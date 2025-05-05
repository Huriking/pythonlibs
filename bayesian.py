from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import TabularCPD

model = DiscreteBayesianNetwork([
    ('Smoking','LungCancer'),
    ('LungCancer','Xray'),
    ('LungCancer','Cough')
])

cpd_smoking = TabularCPD(variable='Smoking',variable_card=2,values=[[0.7],[0.3]])
cpd_lungcancer = TabularCPD(variable='LungCancer',variable_card=2,values=[[0.99,0.9],[0.01,0.1]],evidence=['Smoking'],evidence_card=[2])
cpd_xray = TabularCPD(variable='Xray',variable_card=2,values=[[0.1,0.9],[0.9,0.1]],evidence=['LungCancer'],evidence_card=[2])
cpd_cough = TabularCPD(variable='Cough',variable_card=2,values=[[0.2,0.8],[0.8,0.2]],evidence=['LungCancer'],evidence_card=[2])


model.add_cpds(cpd_smoking,cpd_lungcancer,cpd_xray,cpd_cough)
inference = VariableElimination(model)

print("Query: What is the probability of Smoking given a positive X-ray?")
result = inference.query(variables=['Smoking'],evidence={'LungCancer':     1})
print(result)