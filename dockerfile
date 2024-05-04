FROM gcc:11.2.0

RUN apt-get update && apt-get install -y \ 
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install typer

RUN git clone --branch v4.0 https://github.com/cpputest/cpputest.git cpputest
RUN cd cpputest && autoreconf . -i && ./configure && make tdd

WORKDIR /project

CMD unit-tests/scripts/entry-point.sh
