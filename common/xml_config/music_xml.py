# ./music_xml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2016-05-26 11:48:58.664322 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d515a1d6-2337-11e6-9038-0242ac110002')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: TargetConnectorType
class TargetConnectorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TargetConnectorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 21, 8)
    _Documentation = None
TargetConnectorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TargetConnectorType, enum_prefix=None)
TargetConnectorType.RPC = TargetConnectorType._CF_enumeration.addEnumeration(unicode_value='RPC', tag='RPC')
TargetConnectorType.Static = TargetConnectorType._CF_enumeration.addEnumeration(unicode_value='Static', tag='Static')
TargetConnectorType._InitializeFacetMap(TargetConnectorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TargetConnectorType', TargetConnectorType)

# Atomic simple type: PortType
class PortType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PortType')
    _XSDLocation = pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 46, 8)
    _Documentation = None
PortType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PortType, enum_prefix=None)
PortType.Event = PortType._CF_enumeration.addEnumeration(unicode_value='Event', tag='Event')
PortType.Continuous = PortType._CF_enumeration.addEnumeration(unicode_value='Continuous', tag='Continuous')
PortType.Message = PortType._CF_enumeration.addEnumeration(unicode_value='Message', tag='Message')
PortType._InitializeFacetMap(PortType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PortType', PortType)

# Complex type RootElement with content type ELEMENT_ONLY
class RootElement (pyxb.binding.basis.complexTypeDefinition):
    """Complex type RootElement with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RootElement')
    _XSDLocation = pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 4, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Connection uses Python identifier Connection
    __Connection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Connection'), 'Connection', '__AbsentNamespace0_RootElement_Connection', True, pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 6, 16), )

    
    Connection = property(__Connection.value, __Connection.set, None, None)

    _ElementMap.update({
        __Connection.name() : __Connection
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RootElement', RootElement)


# Complex type ConnectionType with content type ELEMENT_ONLY
class ConnectionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ConnectionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConnectionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 10, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_ConnectionType_type', False, pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 12, 16), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element portname uses Python identifier portname
    __portname = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'portname'), 'portname', '__AbsentNamespace0_ConnectionType_portname', False, pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 13, 16), )

    
    portname = property(__portname.value, __portname.set, None, None)

    
    # Element connector uses Python identifier connector
    __connector = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'connector'), 'connector', '__AbsentNamespace0_ConnectionType_connector', False, pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 14, 16), )

    
    connector = property(__connector.value, __connector.set, None, None)

    
    # Element width uses Python identifier width
    __width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__AbsentNamespace0_ConnectionType_width', False, pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 15, 16), )

    
    width = property(__width.value, __width.set, None, None)

    
    # Element sender uses Python identifier sender
    __sender = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sender'), 'sender', '__AbsentNamespace0_ConnectionType_sender', False, pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 16, 16), )

    
    sender = property(__sender.value, __sender.set, None, None)

    
    # Element receiver uses Python identifier receiver
    __receiver = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'receiver'), 'receiver', '__AbsentNamespace0_ConnectionType_receiver', True, pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 17, 16), )

    
    receiver = property(__receiver.value, __receiver.set, None, None)

    _ElementMap.update({
        __type.name() : __type,
        __portname.name() : __portname,
        __connector.name() : __connector,
        __width.name() : __width,
        __sender.name() : __sender,
        __receiver.name() : __receiver
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ConnectionType', ConnectionType)


# Complex type PeerType with content type ELEMENT_ONLY
class PeerType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type PeerType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PeerType')
    _XSDLocation = pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 28, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_PeerType_name', False, pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 30, 16), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element target uses Python identifier target
    __target = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'target'), 'target', '__AbsentNamespace0_PeerType_target', True, pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 31, 16), )

    
    target = property(__target.value, __target.set, None, None)

    
    # Element parameters uses Python identifier parameters
    __parameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'parameters'), 'parameters', '__AbsentNamespace0_PeerType_parameters', False, pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 32, 16), )

    
    parameters = property(__parameters.value, __parameters.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __target.name() : __target,
        __parameters.name() : __parameters
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'PeerType', PeerType)


# Complex type ParameterList with content type ELEMENT_ONLY
class ParameterList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ParameterList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ParameterList')
    _XSDLocation = pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 36, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'parameter'), 'parameter', '__AbsentNamespace0_ParameterList_parameter', True, pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 38, 16), )

    
    parameter = property(__parameter.value, __parameter.set, None, None)

    _ElementMap.update({
        __parameter.name() : __parameter
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ParameterList', ParameterList)


# Complex type ParameterType with content type MIXED
class ParameterType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ParameterType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ParameterType')
    _XSDLocation = pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 42, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_ParameterType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 43, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 43, 12)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'ParameterType', ParameterType)


Root = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Root'), RootElement, location=pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 3, 4))
Namespace.addCategoryObject('elementBinding', Root.name().localName(), Root)



RootElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Connection'), ConnectionType, scope=RootElement, location=pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 6, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 6, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RootElement._UseForTag(pyxb.namespace.ExpandedName(None, 'Connection')), pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 6, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RootElement._Automaton = _BuildAutomaton()




ConnectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), PortType, scope=ConnectionType, location=pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 12, 16)))

ConnectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'portname'), pyxb.binding.datatypes.string, scope=ConnectionType, location=pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 13, 16)))

ConnectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'connector'), TargetConnectorType, scope=ConnectionType, location=pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 14, 16)))

ConnectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'width'), pyxb.binding.datatypes.integer, scope=ConnectionType, location=pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 15, 16)))

ConnectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sender'), PeerType, scope=ConnectionType, location=pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 16, 16)))

ConnectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'receiver'), PeerType, scope=ConnectionType, location=pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 17, 16)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConnectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 12, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConnectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'portname')), pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 13, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConnectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'connector')), pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 14, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConnectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'width')), pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 15, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConnectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'sender')), pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 16, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConnectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'receiver')), pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 17, 16))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ConnectionType._Automaton = _BuildAutomaton_()




PeerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=PeerType, location=pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 30, 16)))

PeerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'target'), pyxb.binding.datatypes.string, scope=PeerType, location=pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 31, 16)))

PeerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'parameters'), ParameterList, scope=PeerType, location=pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 32, 16)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 31, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 32, 16))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PeerType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 30, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PeerType._UseForTag(pyxb.namespace.ExpandedName(None, 'target')), pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 31, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PeerType._UseForTag(pyxb.namespace.ExpandedName(None, 'parameters')), pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 32, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PeerType._Automaton = _BuildAutomaton_2()




ParameterList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'parameter'), ParameterType, scope=ParameterList, location=pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 38, 16)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ParameterList._UseForTag(pyxb.namespace.ExpandedName(None, 'parameter')), pyxb.utils.utility.Location('/home/packages/music_wizard/common/xml_config/music.xsd', 38, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ParameterList._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
ParameterType._Automaton = _BuildAutomaton_4()

