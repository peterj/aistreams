# Episode 12: Deploy and run Embedchain apps on Kubernetes - Part 2

[YouTube](https://youtube.com/live/q2sG9cRJh-w)

The saga continues!

Last time, I built the basic Docker image that packages the Embedchain app and the YAML files for deploying it to the Kubernetes cluster. In the current setup, we can configure the container with a ConfigMap (for configuration) and a Secret (for the OpenAI API key). We ended the stream with basic scaffolding for the Kubernetes controller.

You can get the repo with everything that we created so far here: https://github.com/peterj/ec-kube

In this stream, I'll continue building the Kubernetes controller.

## Resources

- Repo: https://github.com/peterj/ec-kube
- Kubernetes: https://kubernetes.io
- Embedchain: https://www.embedchain.ai/
