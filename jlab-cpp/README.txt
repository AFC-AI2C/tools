To obtain container:
docker pull afcai2c/jlab-cpp

To list container:
docker images

To run container:
docker run -it -p 8282:8282 {image_id}

When in container's bash:
jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8282 --no-browser --allow-root

Open a browser and go to the url provided by the container
From the "New" dropdown in the top-right, select a kernel (C++ version 11, 14, or 17)
