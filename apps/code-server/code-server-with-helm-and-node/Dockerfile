FROM codercom/code-server:4.95.3
#FROM dockerhub.devops.telekom.de/codercom/code-server:4.95.3

USER 0

ARG KCVERSION=v1.31.3
ARG KCSHA256=981f6b49577068bc174275184d8ee7105d8e54f40733792c519cd85023984c0f

ARG HELMVERSION=v3.16.3
ARG HELMSHA256=f5355c79190951eed23c5432a3b920e071f4c00a64f75e077de0dd4cb7b294ea

ARG NODEVERSION=v22.11.0


# ----- INSTALL "kubectl" ----- (see https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/ )
RUN set -xv && curl -Lo /usr/local/bin/kubectl https://dl.k8s.io/release/$KCVERSION/bin/linux/amd64/kubectl \
    && echo $KCSHA256 \
    && sha256sum /usr/local/bin/kubectl \
    && echo "$KCSHA256  /usr/local/bin/kubectl" | sha256sum -c \
    && chmod a+x /usr/local/bin/kubectl

# ----- INSTALL "helm" ----- (see https://github.com/helm/helm/releases )
RUN cd /tmp \
    && curl -Lo helm.tar.gz https://get.helm.sh/helm-${HELMVERSION}-linux-amd64.tar.gz \
    && echo "$HELMSHA256  helm.tar.gz" | sha256sum -c \
    && tar xvzf helm.tar.gz \
    && cp linux-amd64/helm /usr/local/bin/ \
    && chmod a+x /usr/local/bin/helm \
    && rm -rf /tmp/linux-amd64 \
    && rm /tmp/*


# ----- INSTALL "node" ----- (see https://joshtronic.com/2023/11/12/how-to-install-node-js-21-on-ubuntu/ )
#                            (update: https://nodejs.org/en/download/package-manager )
RUN apt update \
    && apt install -y ca-certificates curl gnupg jq \
    && curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash \
    && export NVM_DIR="$HOME/.nvm" \
    && . "$NVM_DIR/nvm.sh"  \    
    && nvm install $NODEVERSION \
    && node -v \
    && npm -v

USER 1000:1000
