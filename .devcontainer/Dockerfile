FROM python:3.12.2-bookworm
COPY requirements.txt .
RUN apt-get update && apt-get install -y coreutils  wget zsh git && pip install --upgrade pip
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh \
  && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
RUN pip install -r requirements.txt