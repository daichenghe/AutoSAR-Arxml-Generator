## Author: junhao.bai
# Date: 2023-12-01 17:14:06
# Last Modified by:   junhao.bai
# Last Modified time: 2023-12-21 20:47:02
#


from .internalBehaviors import InternalBehaviors
from lxml import etree


def create_internal_behaviors_xml(
    internal_behaviors: InternalBehaviors, application_sw_component_type
):
    # INTERNAL-BEHAVIORS
    internal_behavior_element = etree.SubElement(
        application_sw_component_type, "INTERNAL-BEHAVIORS"
    )
    swc_internal_behavior_el = etree.SubElement(
        internal_behavior_element, "SWC-INTERNAL-BEHAVIOR"
    )
    swc_internal_behavior_el.attrib[
        "UUID"
    ] = internal_behaviors.swc_internal_behavior.UUID
    short_name_el = etree.SubElement(swc_internal_behavior_el, "SHORT-NAME")
    short_name_el.text = internal_behaviors.swc_internal_behavior.short_name

    # Create RUNNABLES and TIMING-EVENTS if they exist in internal_behaviors
    if internal_behaviors.swc_internal_behavior.runnables:
        runnables_el = etree.SubElement(swc_internal_behavior_el, "RUNNABLES")
        for (
            runnable
        ) in internal_behaviors.swc_internal_behavior.runnables.runnable_entity:
            runnable_el = etree.SubElement(runnables_el, "RUNNABLE-ENTITY")
            runnable_el.attrib["UUID"] = runnable.UUID

            short_name_el = etree.SubElement(runnable_el, "SHORT-NAME")
            short_name_el.text = runnable.short_name

            can_be_invoked_concurrently_el = etree.SubElement(
                runnable_el, "CAN-BE-INVOKED-CONCURRENTLY"
            )
            can_be_invoked_concurrently_el.text = str(
                runnable.can_be_invoked_concurrently
            ).lower()

            # Serialize DATA-RECEIVE-POINT-BY-ARGUMENTS
            if runnable.data_receive_point_by_arguments:
                drpba_el = etree.SubElement(
                    runnable_el, "DATA-RECEIVE-POINT-BY-ARGUMENTS"
                )
                for (
                    var_access
                ) in runnable.data_receive_point_by_arguments.variable_access:
                    var_access_el = etree.SubElement(drpba_el, "VARIABLE-ACCESS")
                    var_access_short_name_el = etree.SubElement(
                        var_access_el, "SHORT-NAME"
                    )
                    var_access_short_name_el.text = var_access.short_name

                    accessed_variable_el = etree.SubElement(
                        var_access_el, "ACCESSED-VARIABLE"
                    )
                    autosar_var_iref_el = etree.SubElement(
                        accessed_variable_el, "AUTOSAR-VARIABLE-IREF"
                    )

                    port_proto_ref_el = etree.SubElement(
                        autosar_var_iref_el, "PORT-PROTOTYPE-REF"
                    )
                    port_proto_ref_el.attrib[
                        "DEST"
                    ] = (
                        var_access.accessed_variable.autosar_variable_iref.port_prototype_ref.dest
                    )
                    port_proto_ref_el.text = (
                        var_access.accessed_variable.autosar_variable_iref.port_prototype_ref.value
                    )

                    target_data_proto_ref_el = etree.SubElement(
                        autosar_var_iref_el, "TARGET-DATA-PROTOTYPE-REF"
                    )
                    target_data_proto_ref_el.attrib[
                        "DEST"
                    ] = (
                        var_access.accessed_variable.autosar_variable_iref.target_data_prototype_ref.dest
                    )
                    target_data_proto_ref_el.text = (
                        var_access.accessed_variable.autosar_variable_iref.target_data_prototype_ref.value
                    )

            # Serialize DATA-SEND-POINTS
            if runnable.data_send_points:
                dsp_el = etree.SubElement(runnable_el, "DATA-SEND-POINTS")
                for var_access in runnable.data_send_points.variable_access:
                    var_access_el = etree.SubElement(dsp_el, "VARIABLE-ACCESS")
                    var_access_short_name_el = etree.SubElement(
                        var_access_el, "SHORT-NAME"
                    )
                    var_access_short_name_el.text = var_access.short_name

                    accessed_variable_el = etree.SubElement(
                        var_access_el, "ACCESSED-VARIABLE"
                    )
                    autosar_var_iref_el = etree.SubElement(
                        accessed_variable_el, "AUTOSAR-VARIABLE-IREF"
                    )

                    port_proto_ref_el = etree.SubElement(
                        autosar_var_iref_el, "PORT-PROTOTYPE-REF"
                    )
                    port_proto_ref_el.attrib[
                        "DEST"
                    ] = (
                        var_access.accessed_variable.autosar_variable_iref.port_prototype_ref.dest
                    )
                    port_proto_ref_el.text = (
                        var_access.accessed_variable.autosar_variable_iref.port_prototype_ref.value
                    )

                    target_data_proto_ref_el = etree.SubElement(
                        autosar_var_iref_el, "TARGET-DATA-PROTOTYPE-REF"
                    )
                    target_data_proto_ref_el.attrib[
                        "DEST"
                    ] = (
                        var_access.accessed_variable.autosar_variable_iref.target_data_prototype_ref.dest
                    )
                    target_data_proto_ref_el.text = (
                        var_access.accessed_variable.autosar_variable_iref.target_data_prototype_ref.value
                    )

            # Serialize SYMBOL if it exists
            if runnable.symbol:
                symbol_el = etree.SubElement(runnable_el, "SYMBOL")
                symbol_el.text = runnable.symbol

    if internal_behaviors.swc_internal_behavior.events:
        events_el = etree.SubElement(swc_internal_behavior_el, "EVENTS")
        # 添加timing event
        for timing_event in internal_behaviors.swc_internal_behavior.events.timing_event:
            timing_event_el = etree.SubElement(events_el, "TIMING-EVENT")
            timing_event_el.attrib["UUID"] = timing_event.UUID

            timing_event_short_name_el = etree.SubElement(timing_event_el, "SHORT-NAME")
            timing_event_short_name_el.text = timing_event.short_name

            period_el = etree.SubElement(timing_event_el, "PERIOD")
            period_el.text = str(timing_event.period)

            start_on_event_ref_el = etree.SubElement(
                timing_event_el, "START-ON-EVENT-REF"
            )
            start_on_event_ref_el.text = timing_event.start_on_event_ref
            start_on_event_ref_el.attrib["DEST"] = timing_event.dest
        # 添加init event
        if internal_behaviors.swc_internal_behavior.events.init_event:
            init_event = internal_behaviors.swc_internal_behavior.events.init_event
            init_event_el = etree.SubElement(events_el, "INIT-EVENT")
            init_event_el.attrib["UUID"] = init_event.UUID

            init_event_short_name_el = etree.SubElement(init_event_el, "SHORT-NAME")
            init_event_short_name_el.text = init_event.short_name

            start_on_event_ref_el = etree.SubElement(
                init_event_el, "START-ON-EVENT-REF"
            )
            start_on_event_ref_el.text = init_event.start_on_event_ref
            start_on_event_ref_el.attrib["DEST"] = init_event.dest
        
        # TODO: 添加data-received-event
        if internal_behaviors.swc_internal_behavior.events.data_received_event:
            for data_received_event in internal_behaviors.swc_internal_behavior.events.data_received_event:
                data_received_event_el = etree.SubElement(events_el, "DATA-RECEIVED-EVENT")
                data_received_event_el.attrib["UUID"] = data_received_event.UUID

                data_received_event_short_name_el = etree.SubElement(data_received_event_el, "SHORT-NAME")
                data_received_event_short_name_el.text = data_received_event.short_name

                start_on_event_ref_el = etree.SubElement(
                    data_received_event_el, "START-ON-EVENT-REF"
                )
                start_on_event_ref_el.text = data_received_event.start_on_event_ref
                start_on_event_ref_el.attrib["DEST"] = 'RUNNABLE-ENTITY'

                data_iref_el = etree.SubElement(
                    data_received_event_el, "DATA-IREF"
                )
                
                context_r_port_ref_el = etree.SubElement(
                    data_iref_el, "CONTEXT-R-PORT-REF"
                )

                target_data_element_ref_el = etree.SubElement(
                    data_iref_el, "TARGET-DATA-ELEMENT-REF"
                )

                context_r_port_ref_el.text = data_received_event.data_iref.context_r_port_ref
                context_r_port_ref_el.attrib["DEST"] = 'R-PORT-PROTOTYPE'
                target_data_element_ref_el.text = data_received_event.data_iref.target_data_element_ref
                target_data_element_ref_el.attrib["DEST"] = 'VARIABLE-DATA-PROTOTYPE'
