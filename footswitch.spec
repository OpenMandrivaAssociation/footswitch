%define sourcedate 20251122

# NOTE To update this package run package-source.sh in order to create
# NOTE a new source tarball from the latest upstream git master branch.
# NOTE The script will adjust sourcedate define to match created tarball date.
# NOTE You may have to reload this file to see the changed value.

Name:		footswitch
# Version:	1.0
Version:	1.0.%{sourcedate}
Release:	1
Summary:	Command-line utility for PCsensor and Scythe USB foot switches
URL:		https://github.com/rgerganov/footswitch
License:	MIT
Group:		System/Utilities
# Source0:	%%{url}/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0:	%{name}-%{sourcedate}.tar.zst

BuildRequires:	cmake
BuildRequires:	cmake(hidapi)
BuildRequires:	ninja
BuildRequires:	pkgconfig

%description
Command line utlities for programming PCsensor and Scythe USB foot switches.

The following list of devices are supported:
vendorId	productId	Program
0c45	7403	footswitch
0c45	7404	footswitch
413d	2107	footswitch
1a86	e026	footswitch
3553	b001	footswitch
0426	3011	scythe
055a	0998	scythe2

You can find the vendorId and productId of your device using the 'lsusb' command.

%prep
%autosetup -n %{name}-%{sourcedate} -p1

# Fix missing udev MODE rule parameters
sed -i -e 's/, TAG+="uaccess"/, MODE="0660", TAG+="uaccess"/g' 19-%{name}.rules

%build
%cmake -G Ninja
%ninja_build

%install
%ninja_install -C build
# install udev rules
install -d -m 0755 %{buildroot}%{_sysconfdir}/udev/rules.d
install -pm 0644 19-%{name}.rules %{buildroot}%{_sysconfdir}/udev/rules.d/

%files
%doc README.md
%license LICENSE
%{_bindir}/footswitch
%{_bindir}/scythe
%{_bindir}/scythe2
%{_sysconfdir}/udev/rules.d/19-%{name}.rules
