''' Creating population and sample numpy arrays '''
import numpy as np
import config_file  # noqa: F401
from utilities.file_utilities import FileUtilities


PATH = FileUtilities.get_abs_path("../../Course_Materials_Part1/Statistics/Course_Materials_Statistics/Video_Lectures_NBs/")  # noqa: E501
population_file = PATH + "SP500_pop.csv"
sample_file = PATH + "sample.csv"

np.set_printoptions(precision=2, suppress=True)

# Population: 2017 Price Return for all 500 Companies
pop = np.loadtxt(population_file, delimiter=",", usecols=1)
# print(pop)
pop = pop * 100  # converting the values in % form as in 47% or -42%
# print(pop)
# print(pop.size)

# Sample: 2017 Price Return for 50 Companies (randomly selected)
sample = np.loadtxt(sample_file, delimiter=",", usecols=1)
sample = sample * 100
# print(sample)
# print(sample.size)
