variable = 'Alvaro'
otra = 'genios estudiantes'

forma = "El profesor '{}' y sus '{}'".format(variable,otra)
print(forma)
forma = "El profesor '{1}' y sus '{0}'".format(variable,otra)
print(forma)
print('{:>50}'.format('Alvaro chrirou'))