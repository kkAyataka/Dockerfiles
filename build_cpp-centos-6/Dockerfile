FROM centos:6

# CentOS 6 was the end of life on 2020/11/30.
RUN sed -i -e "s/^mirrorlist=http:/#mirrorlist=http:/g" /etc/yum.repos.d/CentOS-Base.repo && \
    sed -i -e "s/^#baseurl=http:\/\/mirror/baseurl=http:\/\/vault/g" /etc/yum.repos.d/CentOS-Base.repo

RUN yum update -y && \
    yum install -y \
        automake \
        gcc-c++ \
        git \
        make
