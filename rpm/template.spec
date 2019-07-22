Name:           ros-melodic-realtime-tools
Version:        1.14.0
Release:        1%{?dist}
Summary:        ROS realtime_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/realtime_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-actionlib
Requires:       ros-melodic-roscpp
BuildRequires:  ros-melodic-actionlib
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-rosunit

%description
Contains a set of tools that can be used from a hard realtime thread, without
breaking the realtime behavior.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Jul 22 2019 Bence Magyar <bence.magyar.robotics@gmail.com> - 1.14.0-1
- Autogenerated by Bloom

* Thu Feb 14 2019 Bence Magyar <bence.magyar.robotics@gmail.com> - 1.13.1-0
- Autogenerated by Bloom

* Mon Feb 11 2019 Bence Magyar <bence.magyar.robotics@gmail.com> - 1.13.0-0
- Autogenerated by Bloom

* Sat May 19 2018 Bence Magyar <bence.magyar.robotics@gmail.com> - 1.12.0-0
- Autogenerated by Bloom

* Mon Mar 19 2018 Stuart Glaser <sglaser@willowgarage.com> - 1.11.0-0
- Autogenerated by Bloom

