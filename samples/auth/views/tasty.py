# Portions (c) 2014, Alexander Klimenko <alex@erix.ru>
# All rights reserved.
#
# Copyright (c) 2011, SmartFile <btimby@smartfile.com>
# All rights reserved.
#
# This file is part of DjangoDav.
#
# DjangoDav is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DjangoDav is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with DjangoDav.  If not, see <http://www.gnu.org/licenses/>.
from tastypie.authentication import \
    BasicAuthentication as TastyBasicAuthentication
from tastypie.authentication import MultiAuthentication
from tastypie.authentication import \
    SessionAuthentication as TastySessionAuthentication

from djangodav.auth.tasty import TastypieAuthViewMixIn
from djangodav.views import DavView


class TastyAuthDavView(TastypieAuthViewMixIn, DavView):
    authentication = MultiAuthentication(
        TastyBasicAuthentication(), TastySessionAuthentication()
    )
