To run container:
docker run -it -p 8282:8282 {image_id}

When in container's bash:
jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8282 --no-browser --allow-root
