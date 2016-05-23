# ./musix_xml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2016-04-20 11:37:14.487174 by PyXB version 1.2.4 using Python 2.7.6.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:76f1ba2c-06db-11e6-a03f-002354bd6608')

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


# Atomic simple type: MusicInPortType
class MusicInPortType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MusicInPortType')
    _XSDLocation = pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 36, 8)
    _Documentation = None
MusicInPortType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MusicInPortType, enum_prefix=None)
MusicInPortType.Cont = MusicInPortType._CF_enumeration.addEnumeration(unicode_value='Cont', tag='Cont')
MusicInPortType.Msg = MusicInPortType._CF_enumeration.addEnumeration(unicode_value='Msg', tag='Msg')
MusicInPortType._InitializeFacetMap(MusicInPortType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MusicInPortType', MusicInPortType)

# Atomic simple type: MusicOutPortType
class MusicOutPortType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MusicOutPortType')
    _XSDLocation = pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 43, 8)
    _Documentation = None
MusicOutPortType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MusicOutPortType, enum_prefix=None)
MusicOutPortType.Cont = MusicOutPortType._CF_enumeration.addEnumeration(unicode_value='Cont', tag='Cont')
MusicOutPortType.Msg = MusicOutPortType._CF_enumeration.addEnumeration(unicode_value='Msg', tag='Msg')
MusicOutPortType._InitializeFacetMap(MusicOutPortType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MusicOutPortType', MusicOutPortType)

# Atomic simple type: ModelType
class ModelType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ModelType')
    _XSDLocation = pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 50, 8)
    _Documentation = None
ModelType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ModelType, enum_prefix=None)
ModelType.ACSource = ModelType._CF_enumeration.addEnumeration(unicode_value='ACSource', tag='ACSource')
ModelType.DCSource = ModelType._CF_enumeration.addEnumeration(unicode_value='DCSource', tag='DCSource')
ModelType.FixedFrequency = ModelType._CF_enumeration.addEnumeration(unicode_value='FixedFrequency', tag='FixedFrequency')
ModelType.LeakyIntegratorAlpha = ModelType._CF_enumeration.addEnumeration(unicode_value='LeakyIntegratorAlpha', tag='LeakyIntegratorAlpha')
ModelType.LeakyIntegratorExp = ModelType._CF_enumeration.addEnumeration(unicode_value='LeakyIntegratorExp', tag='LeakyIntegratorExp')
ModelType.NCSource = ModelType._CF_enumeration.addEnumeration(unicode_value='NCSource', tag='NCSource')
ModelType.Poisson = ModelType._CF_enumeration.addEnumeration(unicode_value='Poisson', tag='Poisson')
ModelType.SpikeRecorder = ModelType._CF_enumeration.addEnumeration(unicode_value='SpikeRecorder', tag='SpikeRecorder')
ModelType.PopulationRate = ModelType._CF_enumeration.addEnumeration(unicode_value='PopulationRate', tag='PopulationRate')
ModelType._InitializeFacetMap(ModelType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ModelType', ModelType)

# Complex type RootElement with content type ELEMENT_ONLY
class RootElement (pyxb.binding.basis.complexTypeDefinition):
    """Complex type RootElement with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RootElement')
    _XSDLocation = pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 6, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Device uses Python identifier Device
    __Device = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Device'), 'Device', '__AbsentNamespace0_RootElement_Device', True, pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 8, 16), )

    
    Device = property(__Device.value, __Device.set, None, None)

    _ElementMap.update({
        __Device.name() : __Device
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RootElement', RootElement)


# Complex type DeviceType with content type ELEMENT_ONLY
class DeviceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DeviceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeviceType')
    _XSDLocation = pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 12, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element portname uses Python identifier portname
    __portname = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'portname'), 'portname', '__AbsentNamespace0_DeviceType_portname', False, pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 14, 12), )

    
    portname = property(__portname.value, __portname.set, None, None)

    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_DeviceType_type', False, pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 15, 12), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element observer uses Python identifier observer
    __observer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'observer'), 'observer', '__AbsentNamespace0_DeviceType_observer', True, pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 16, 12), )

    
    observer = property(__observer.value, __observer.set, None, None)

    
    # Element setter uses Python identifier setter
    __setter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'setter'), 'setter', '__AbsentNamespace0_DeviceType_setter', True, pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 17, 12), )

    
    setter = property(__setter.value, __setter.set, None, None)

    _ElementMap.update({
        __portname.name() : __portname,
        __type.name() : __type,
        __observer.name() : __observer,
        __setter.name() : __setter
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DeviceType', DeviceType)


# Complex type Observer with content type ELEMENT_ONLY
class Observer (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Observer with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Observer')
    _XSDLocation = pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 21, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_Observer_type', False, pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 23, 14), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'property'), 'property_', '__AbsentNamespace0_Observer_property', False, pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 24, 12), )

    
    property_ = property(__property.value, __property.set, None, None)

    _ElementMap.update({
        __type.name() : __type,
        __property.name() : __property
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Observer', Observer)


# Complex type Setter with content type ELEMENT_ONLY
class Setter (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Setter with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Setter')
    _XSDLocation = pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 28, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_Setter_type', False, pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 30, 14), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'property'), 'property_', '__AbsentNamespace0_Setter_property', False, pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 31, 14), )

    
    property_ = property(__property.value, __property.set, None, None)

    _ElementMap.update({
        __type.name() : __type,
        __property.name() : __property
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Setter', Setter)


Root = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Root'), RootElement, location=pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 4, 4))
Namespace.addCategoryObject('elementBinding', Root.name().localName(), Root)



RootElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Device'), DeviceType, scope=RootElement, location=pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 8, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 8, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RootElement._UseForTag(pyxb.namespace.ExpandedName(None, 'Device')), pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 8, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RootElement._Automaton = _BuildAutomaton()




DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'portname'), pyxb.binding.datatypes.string, scope=DeviceType, location=pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 14, 12)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), ModelType, scope=DeviceType, location=pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 15, 12)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'observer'), Observer, scope=DeviceType, location=pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 16, 12)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'setter'), Setter, scope=DeviceType, location=pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 17, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 16, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 17, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'portname')), pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 14, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 15, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'observer')), pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 16, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'setter')), pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 17, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DeviceType._Automaton = _BuildAutomaton_()




Observer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), MusicOutPortType, scope=Observer, location=pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 23, 14)))

Observer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'property'), pyxb.binding.datatypes.string, scope=Observer, location=pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 24, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Observer._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 23, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Observer._UseForTag(pyxb.namespace.ExpandedName(None, 'property')), pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 24, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Observer._Automaton = _BuildAutomaton_2()




Setter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), MusicInPortType, scope=Setter, location=pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 30, 14)))

Setter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'property'), pyxb.binding.datatypes.string, scope=Setter, location=pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 31, 14)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Setter._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 30, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Setter._UseForTag(pyxb.namespace.ExpandedName(None, 'property')), pyxb.utils.utility.Location('/disk/no_backup/schulze/NRP_32/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/music/simulator_backend/xml_config/music.xsd', 31, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Setter._Automaton = _BuildAutomaton_3()

