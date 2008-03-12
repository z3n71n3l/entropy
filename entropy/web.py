from zope.interface import implements

from axiom.item import Item
from axiom.attributes import text, path
from axiom.dependency import dependsOn

from xmantissa.ixmantissa import IProtocolFactoryFactory
from xmantissa.website import AxiomSite

from entropy.util import getAppStore


# FIXME: This is a blatant rip from Mantissa's code, necessary in order to
# customize the root of the site, to avoid having guard wrapped around it.

class SimpleSiteFactory(Item):
    """
    Configuration object for a Mantissa HTTP server.
    """
    powerupInterfaces = [IProtocolFactoryFactory]
    implements(*powerupInterfaces)

    loginSystem = dependsOn(LoginSystem)

    httpLog = path(default=None)

    def getFactory(self):
        """
        Create an L{AxiomSite} which supports authenticated and anonymous
        access.
        """
        logPath = self.httpLog and self.httpLog.path
        appStore = getAppStore(self.store)
        return AxiomSite(appStore, IResource(appStore), logPath=logPath)
