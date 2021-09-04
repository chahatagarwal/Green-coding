Green coding
******

This repository is just for learning/experimental purpose in order to try something different and be habitual for day to day routines

Reference
------------
@article{codecarbon, author={Victor Schmidt and Kamal Goyal and Aditya Joshi and Boris Feld and Liam Conell and Nikolas Laskaris and Doug Blank and Jonathan Wilson and Sorelle Friedler and Sasha Luccioni}, title={{CodeCarbon: Estimate and Track Carbon Emissions from Machine Learning Computing}}, year={2021}, howpublished={\url{https://github.com/mlco2/codecarbon}}, DOI={10.5281/zenodo.4658424}, publisher={Zenodo}, }

Dependencies
-------------
Create a virtual environment using conda for easier management of dependencies and packages.

For installing conda, follow the instructions on the official conda website

-> conda create --name codecarbon python=3.6

-> conda activate codecarbon (OR) activate codecarbon

Then install codecarbon from PyPI repository

-> pip install codecarbon

Install from Conda repository

-> conda install -c codecarbon -c conda-forge codecarbon.

Infrastructure Support
-----------------------
Currently, the package supports the following hardware infrastructure.

GPU
Tracks Nvidia GPUs power consumption using pynvml library, (which is installed with the package).

CPU
On Windows and Mac
Tracks Intel processors power consumption using the Intel Power Gadget. You need to install it independently for CodeCarbon to function.

Note: Please ensure that the Intel Power Gadget has the required security permissions on macOS.

On Linux
Tracks Intel Processors power consumption from Intel RAPL files at /sys/class/powercap/intel-rapl. All CPUs listed in this directory will be tracked. Help us improve this and make it configurable.

Note: The Power Consumption will be tracked only if the RAPL files exist at the above-mentioned path.

On all platforms
If CodeCarbon cannot find the appropriate software to track the CPUs' energy consumption, it will use a fallback strategy:

Find TDP
------------
If it can match your cpu type to a list of 2000+ Intel and AMD CPUs it will retrieve its thermal design power (TDPs). Link of Supported processors: https://github.com/mlco2/codecarbon/blob/master/codecarbon/data/hardware/cpu_power.csv

If it really can't tell anything about your CPU it will use a constant TDP of 85W. CodeCarbon assumes that the (average) actual power consumption of CPUs will be 50% of their TDP.

Based on the "emissions.csv" file generated, we could use a Built-in visualization tool with the below command
---------------------------
-> carbonboard --filepath="emissions.csv" --port=xxxx (Change path of emissions.csv based on availability to fetch from respective directory)

Online Mode
---------------
from codecarbon import EmissionsTracker

with EmissionsTracker() as tracker: # GPU Intensive code goes here

NOTE
----------
(All personal observation and it would vary for each other's perspective)

- Online vs Offline mode - Benefit of online is to collect various other information available compared to offline.
- In general, it creates a "emissions.csv" irrective of any mode of execution
- Few paramerers could be configured, in order to have single experiment ID or Emission location, etc
- It's better to Flush data when running to store intermediate data By default, Code Carbon only writes the CVS output file when it stops. But for a long run you may want to save intermediate data. It is possible to call the flush() method to do so.
- Use Online Mode + Flush() + Built-in Dashboard for ease and better visualization

Device Details
-----------
- Country: India
- State: Tamil Nadu
- City: Chennai
- Machine Type: Laptop
- TDP: 25W
- RAM: 16GB RAM(DDR4)
- Graphic Card: 4GB Nvidia GeForce MX250
- OS Windows 10
- Processor: Intel Core i7-1065

******************************
I will be trying different Algorithm & Approach in Machine Learning. I will use the same repository to verify the Co2 emission accross different cities to start with from india. Please find the Tabular data for your inference and try finding if you could find some meaningful insights :)
