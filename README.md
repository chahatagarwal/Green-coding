#Green Coding
This repository is just for learning/experimental purpose in order to try something different and be habitual for day to day routines

@article{codecarbon,
  author={Victor Schmidt and Kamal Goyal and Aditya Joshi and Boris Feld and Liam Conell and Nikolas Laskaris and Doug Blank and Jonathan Wilson and Sorelle Friedler and Sasha Luccioni},
  title={{CodeCarbon: Estimate and Track Carbon Emissions from Machine Learning Computing}},
  year={2021},
  howpublished={\url{https://github.com/mlco2/codecarbon}},
  DOI={10.5281/zenodo.4658424},
  publisher={Zenodo},
}

Dependencies:
Create a virtual environment using conda for easier management of dependencies and packages. 
For installing conda, follow the instructions on the official conda website

-> conda create --name codecarbon python=3.6
-> conda activate codecarbon (OR) activate codecarbon

Then install codecarbon from PyPI repository
-> pip install codecarbon
(OR)
Install from Conda repository
-> conda install -c codecarbon -c conda-forge codecarbon.


Infrastructure Support
Currently the package supports following hardware infrastructure.

GPU
Tracks Nvidia GPUs power consumption using pynvml library, (which is installed with the package).

CPU
On Windows and Mac
Tracks Intel processors power consumption using the Intel Power Gadget

You need to install it independently for CodeCarbon to function.
Note: Please ensure that the Intel Power Gadget has the required security permissions on MacOS.

On Linux
Tracks Intel Processors power consumption from Intel RAPL files at /sys/class/powercap/intel-rapl
All CPUs listed in this directory will be tracked. Help us improve this and make it configurable.
Note: The Power Consumption will be tracked only if the RAPL files exist at the above mentioned path.

On all platforms
If CodeCarbon cannot find the appropriate software to track the CPUs' energy consumption, it will use a fallback strategy:

Find TDP:
If it can match your cpu type to a list of 2000+ Intel and AMD CPUs it will retrieve its thermal design power (TDPs)
Link of Supported processors: https://github.com/mlco2/codecarbon/blob/master/codecarbon/data/hardware/cpu_power.csv
If it really can't tell anything about your CPU it will use a constant TDP of 85W
CodeCarbon assumes that the (average) actual power consumption of CPUs will be 50% of their TDP.

Based on "emissions.csv" file generated, we could use Built-in visulaization tool with the below command:
-> carbonboard --filepath="emissions.csv" --port=xxxx (Change path of emissions.csv based on availability to fetch from respective directory)

Online Mode:
from codecarbon import EmissionsTracker

with EmissionsTracker() as tracker:
    # GPU Intensive code goes here

NOTE:
(All personal observation and it would vary for each other's prespective)
- Online vs Offline mode
Benefit of online is to collect various other information available compared to offline.
- In general, it creates a "emissions.csv" irrective of any mode of execution
- Few paramerers could be configured, in order to have single experiment ID or Emission location, etc
- It's better to Flush data when running to store intermediate data
  By default, Code Carbon only writes the CVS output file when it stops. But for a long run you may want to save intermediate data. It is possible to call the flush() method to do so.
- Use Online Mode + Flush() + Built-in Dashboard for ease and better visualization
 
Device Details:
Country: India
State: Tamil Nadu
City: Chennai
Machine Type: Laptop
TDP: 25W
RAM: 16GB RAM(DDR4)
Graphic Card: 4GB Nvidia GeForce MX250
OS Windows 10
Processor: Intel Core i7-1065

I will be trying different Algorithm & Approach in Machine Learning. I will use the same repository to verify the Co2 emission accross different cities to start with from india.
Please find the Tabular data for your inference and try finding if you could find some meaningful insights :)

Callback Approach including flush():
import tensorflow as tf
from tensorflow.keras.callbacks import Callback
from codecarbon import EmissionsTracker

"""
This sample code shows how to use CodeCarbon as a Keras Callback
to save emissions after each epoch.
"""

class CodeCarbonCallBack(Callback):
    def __init__(self, codecarbon_tracker):
        self.codecarbon_tracker = codecarbon_tracker
        pass

    def on_epoch_end(self, epoch, logs=None):
        self.codecarbon_tracker.flush()


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10),
    ]
)

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])

tracker = EmissionsTracker()
tracker.start()
codecarbon_cb = CodeCarbonCallBack(tracker)
model.fit(x_train, y_train, epochs=4, callbacks=[codecarbon_cb])
emissions: float = tracker.stop()
print(f"Emissions: {emissions} kg")
