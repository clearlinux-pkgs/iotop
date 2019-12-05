#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iotop
Version  : 1
Release  : 23
URL      : https://repo.or.cz/iotop.git/snapshot/7c51ce0e29bd135c216f18e18f0c4ab769af0d6f.tar.gz
Source0  : https://repo.or.cz/iotop.git/snapshot/7c51ce0e29bd135c216f18e18f0c4ab769af0d6f.tar.gz
Summary  : View I/O usage of processes
Group    : Development/Tools
License  : GPL-2.0
Requires: iotop-bin = %{version}-%{release}
Requires: iotop-license = %{version}-%{release}
Requires: iotop-man = %{version}-%{release}
Requires: iotop-python = %{version}-%{release}
Requires: iotop-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Iotop is a Python program with a top like UI used to show of behalf of which
process is the I/O going on. It requires Python >= 2.7 and a Linux kernel >=
2.6.20 with the CONFIG_TASK_DELAY_ACCT CONFIG_TASKSTATS,
CONFIG_TASK_IO_ACCOUNTING and CONFIG_VM_EVENT_COUNTERS options on.

%package bin
Summary: bin components for the iotop package.
Group: Binaries
Requires: iotop-license = %{version}-%{release}

%description bin
bin components for the iotop package.


%package license
Summary: license components for the iotop package.
Group: Default

%description license
license components for the iotop package.


%package man
Summary: man components for the iotop package.
Group: Default

%description man
man components for the iotop package.


%package python
Summary: python components for the iotop package.
Group: Default
Requires: iotop-python3 = %{version}-%{release}

%description python
python components for the iotop package.


%package python3
Summary: python3 components for the iotop package.
Group: Default
Requires: python3-core

%description python3
python3 components for the iotop package.


%prep
%setup -q -n iotop-7c51ce0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1553990003
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/iotop
cp COPYING %{buildroot}/usr/share/package-licenses/iotop/COPYING
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
mv %{buildroot}/usr/sbin %{buildroot}/usr/bin
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/iotop

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/iotop/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/iotop.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
