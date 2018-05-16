#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iotop
Version  : 0.6
Release  : 17
URL      : http://guichaz.free.fr/iotop/files/iotop-0.6.tar.bz2
Source0  : http://guichaz.free.fr/iotop/files/iotop-0.6.tar.bz2
Summary  : Per process I/O bandwidth monitor
Group    : Development/Tools
License  : GPL-2.0
Requires: iotop-python
Requires: iotop-bin
Requires: iotop-doc
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
Iotop is a Python program with a top like UI used to show of behalf of which
process is the I/O going on. It requires Python >= 2.7 and a Linux kernel >=
2.6.20 with the CONFIG_TASK_DELAY_ACCT CONFIG_TASKSTATS,
CONFIG_TASK_IO_ACCOUNTING and CONFIG_VM_EVENT_COUNTERS options on.

%package bin
Summary: bin components for the iotop package.
Group: Binaries

%description bin
bin components for the iotop package.


%package doc
Summary: doc components for the iotop package.
Group: Documentation

%description doc
doc components for the iotop package.


%package python
Summary: python components for the iotop package.
Group: Default

%description python
python components for the iotop package.


%prep
%setup -q -n iotop-0.6

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/sbin/iotop

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
