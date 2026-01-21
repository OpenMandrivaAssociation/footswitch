%define sourcedate 20260121
%define gitcommit 42b002d

%bcond packagedsources 1
# NOTE To update this package run package-source.sh in order to create
# NOTE a new source tarball from the latest upstream git master branch.
# NOTE The script will adjust sourcedate & gitcommit defines to match created tarball date.
# NOTE You may have to reload this file to see the changed values.

Name:		footswitch
Release:	1
Summary:	Command-line utility for PCsensor and Scythe USB foot switches
URL:		https://github.com/rgerganov/footswitch
License:	MIT
Group:		System/Utilities
%if %{with packagedsources}
Version:	1.1~%{sourcedate}.git%{gitcommit}
Source0:	%{name}-%{sourcedate}-%{gitcommit}.tar.zst
%else
Version:	1.1
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif
BuildSystem:	cmake
BuildOption:	-G Ninja
BuildRequires:	cmake
BuildRequires:	cmake(hidapi)
BuildRequires:	ninja
BuildRequires:	pkgconfig

%description
Command line utlities for programming PCsensor and Scythe USB foot switches.

The following list of devices are supported:
vendorId  productId  Program
0c45  7403  footswitch
0c45  7404  footswitch
413d  2107  footswitch
1a86  e026  footswitch
3553  b001  footswitch
0426  3011  scythe
055a  0998  scythe2
5131  2019  footswitch1p

You can find the vendorId and productId of your device using the 'lsusb' command.

%prep
%if %{with packagedsources}
%autosetup -n %{name}-%{sourcedate}-%{gitcommit} -p1
%else
%autosetup -p1
%endif
# Fix missing udev MODE rule parameters
sed -i -e 's/, TAG+="uaccess"/, MODE="0660", TAG+="uaccess"/g' 19-%{name}.rules

%install -a
# install udev rules
install -Dpm 0644 19-%{name}.rules %{buildroot}%{_udevrulesdir}/19-%{name}.rules

%files
%doc README.md
%license LICENSE
%{_bindir}/footswitch
%{_bindir}/footswitch1p
%{_bindir}/scythe
%{_bindir}/scythe2
%{_udevrulesdir}/19-%{name}.rules
