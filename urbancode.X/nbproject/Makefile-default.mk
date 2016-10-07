#
# Generated Makefile - do not edit!
#
# Edit the Makefile in the project folder instead (../Makefile). Each target
# has a -pre and a -post target defined where you can add customized code.
#
# This makefile implements configuration specific macros and targets.


# Include project Makefile
ifeq "${IGNORE_LOCAL}" "TRUE"
# do not include local makefile. User is passing all local related variables already
else
include Makefile
# Include makefile containing local settings
ifeq "$(wildcard nbproject/Makefile-local-default.mk)" "nbproject/Makefile-local-default.mk"
include nbproject/Makefile-local-default.mk
endif
endif

# Environment
MKDIR=gnumkdir -p
RM=rm -f 
MV=mv 
CP=cp 

# Macros
CND_CONF=default
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
IMAGE_TYPE=debug
OUTPUT_SUFFIX=elf
DEBUGGABLE_SUFFIX=elf
FINAL_IMAGE=dist/${CND_CONF}/${IMAGE_TYPE}/urbancode.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}
else
IMAGE_TYPE=production
OUTPUT_SUFFIX=hex
DEBUGGABLE_SUFFIX=elf
FINAL_IMAGE=dist/${CND_CONF}/${IMAGE_TYPE}/urbancode.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}
endif

# Object Directory
OBJECTDIR=build/${CND_CONF}/${IMAGE_TYPE}

# Distribution Directory
DISTDIR=dist/${CND_CONF}/${IMAGE_TYPE}

# Source Files Quoted if spaced
SOURCEFILES_QUOTED_IF_SPACED=main.c init.c confbits.c gps_led.c spi_rx.c timer1_handler.c gps_button_handler.c serial.c eeprom.c check_gps_input.c gps_utils.c gps_rx.c uart_rx.c error.c parsefloat.c acknowledge.c check_uart_input.c setup_leds_oc.c get_waypoint.c distance.c game_timer.c hypot.c smooth.c set_leds_pct.c erase.c

# Object Files Quoted if spaced
OBJECTFILES_QUOTED_IF_SPACED=${OBJECTDIR}/main.o ${OBJECTDIR}/init.o ${OBJECTDIR}/confbits.o ${OBJECTDIR}/gps_led.o ${OBJECTDIR}/spi_rx.o ${OBJECTDIR}/timer1_handler.o ${OBJECTDIR}/gps_button_handler.o ${OBJECTDIR}/serial.o ${OBJECTDIR}/eeprom.o ${OBJECTDIR}/check_gps_input.o ${OBJECTDIR}/gps_utils.o ${OBJECTDIR}/gps_rx.o ${OBJECTDIR}/uart_rx.o ${OBJECTDIR}/error.o ${OBJECTDIR}/parsefloat.o ${OBJECTDIR}/acknowledge.o ${OBJECTDIR}/check_uart_input.o ${OBJECTDIR}/setup_leds_oc.o ${OBJECTDIR}/get_waypoint.o ${OBJECTDIR}/distance.o ${OBJECTDIR}/game_timer.o ${OBJECTDIR}/hypot.o ${OBJECTDIR}/smooth.o ${OBJECTDIR}/set_leds_pct.o ${OBJECTDIR}/erase.o
POSSIBLE_DEPFILES=${OBJECTDIR}/main.o.d ${OBJECTDIR}/init.o.d ${OBJECTDIR}/confbits.o.d ${OBJECTDIR}/gps_led.o.d ${OBJECTDIR}/spi_rx.o.d ${OBJECTDIR}/timer1_handler.o.d ${OBJECTDIR}/gps_button_handler.o.d ${OBJECTDIR}/serial.o.d ${OBJECTDIR}/eeprom.o.d ${OBJECTDIR}/check_gps_input.o.d ${OBJECTDIR}/gps_utils.o.d ${OBJECTDIR}/gps_rx.o.d ${OBJECTDIR}/uart_rx.o.d ${OBJECTDIR}/error.o.d ${OBJECTDIR}/parsefloat.o.d ${OBJECTDIR}/acknowledge.o.d ${OBJECTDIR}/check_uart_input.o.d ${OBJECTDIR}/setup_leds_oc.o.d ${OBJECTDIR}/get_waypoint.o.d ${OBJECTDIR}/distance.o.d ${OBJECTDIR}/game_timer.o.d ${OBJECTDIR}/hypot.o.d ${OBJECTDIR}/smooth.o.d ${OBJECTDIR}/set_leds_pct.o.d ${OBJECTDIR}/erase.o.d

# Object Files
OBJECTFILES=${OBJECTDIR}/main.o ${OBJECTDIR}/init.o ${OBJECTDIR}/confbits.o ${OBJECTDIR}/gps_led.o ${OBJECTDIR}/spi_rx.o ${OBJECTDIR}/timer1_handler.o ${OBJECTDIR}/gps_button_handler.o ${OBJECTDIR}/serial.o ${OBJECTDIR}/eeprom.o ${OBJECTDIR}/check_gps_input.o ${OBJECTDIR}/gps_utils.o ${OBJECTDIR}/gps_rx.o ${OBJECTDIR}/uart_rx.o ${OBJECTDIR}/error.o ${OBJECTDIR}/parsefloat.o ${OBJECTDIR}/acknowledge.o ${OBJECTDIR}/check_uart_input.o ${OBJECTDIR}/setup_leds_oc.o ${OBJECTDIR}/get_waypoint.o ${OBJECTDIR}/distance.o ${OBJECTDIR}/game_timer.o ${OBJECTDIR}/hypot.o ${OBJECTDIR}/smooth.o ${OBJECTDIR}/set_leds_pct.o ${OBJECTDIR}/erase.o

# Source Files
SOURCEFILES=main.c init.c confbits.c gps_led.c spi_rx.c timer1_handler.c gps_button_handler.c serial.c eeprom.c check_gps_input.c gps_utils.c gps_rx.c uart_rx.c error.c parsefloat.c acknowledge.c check_uart_input.c setup_leds_oc.c get_waypoint.c distance.c game_timer.c hypot.c smooth.c set_leds_pct.c erase.c


CFLAGS=
ASFLAGS=
LDLIBSOPTIONS=

############# Tool locations ##########################################
# If you copy a project from one host to another, the path where the  #
# compiler is installed may be different.                             #
# If you open this project with MPLAB X in the new host, this         #
# makefile will be regenerated and the paths will be corrected.       #
#######################################################################
# fixDeps replaces a bunch of sed/cat/printf statements that slow down the build
FIXDEPS=fixDeps

.build-conf:  ${BUILD_SUBPROJECTS}
ifneq ($(INFORMATION_MESSAGE), )
	@echo $(INFORMATION_MESSAGE)
endif
	${MAKE}  -f nbproject/Makefile-default.mk dist/${CND_CONF}/${IMAGE_TYPE}/urbancode.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}

MP_PROCESSOR_OPTION=32MX150F128B
MP_LINKER_FILE_OPTION=
# ------------------------------------------------------------------------------------
# Rules for buildStep: assemble
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
else
endif

# ------------------------------------------------------------------------------------
# Rules for buildStep: assembleWithPreprocess
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
else
endif

# ------------------------------------------------------------------------------------
# Rules for buildStep: compile
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
${OBJECTDIR}/main.o: main.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/main.o.d 
	@${RM} ${OBJECTDIR}/main.o 
	@${FIXDEPS} "${OBJECTDIR}/main.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/main.o.d" -o ${OBJECTDIR}/main.o main.c   
	
${OBJECTDIR}/init.o: init.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/init.o.d 
	@${RM} ${OBJECTDIR}/init.o 
	@${FIXDEPS} "${OBJECTDIR}/init.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/init.o.d" -o ${OBJECTDIR}/init.o init.c   
	
${OBJECTDIR}/confbits.o: confbits.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/confbits.o.d 
	@${RM} ${OBJECTDIR}/confbits.o 
	@${FIXDEPS} "${OBJECTDIR}/confbits.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/confbits.o.d" -o ${OBJECTDIR}/confbits.o confbits.c   
	
${OBJECTDIR}/gps_led.o: gps_led.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/gps_led.o.d 
	@${RM} ${OBJECTDIR}/gps_led.o 
	@${FIXDEPS} "${OBJECTDIR}/gps_led.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/gps_led.o.d" -o ${OBJECTDIR}/gps_led.o gps_led.c   
	
${OBJECTDIR}/spi_rx.o: spi_rx.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/spi_rx.o.d 
	@${RM} ${OBJECTDIR}/spi_rx.o 
	@${FIXDEPS} "${OBJECTDIR}/spi_rx.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/spi_rx.o.d" -o ${OBJECTDIR}/spi_rx.o spi_rx.c   
	
${OBJECTDIR}/timer1_handler.o: timer1_handler.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/timer1_handler.o.d 
	@${RM} ${OBJECTDIR}/timer1_handler.o 
	@${FIXDEPS} "${OBJECTDIR}/timer1_handler.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/timer1_handler.o.d" -o ${OBJECTDIR}/timer1_handler.o timer1_handler.c   
	
${OBJECTDIR}/gps_button_handler.o: gps_button_handler.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/gps_button_handler.o.d 
	@${RM} ${OBJECTDIR}/gps_button_handler.o 
	@${FIXDEPS} "${OBJECTDIR}/gps_button_handler.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/gps_button_handler.o.d" -o ${OBJECTDIR}/gps_button_handler.o gps_button_handler.c   
	
${OBJECTDIR}/serial.o: serial.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/serial.o.d 
	@${RM} ${OBJECTDIR}/serial.o 
	@${FIXDEPS} "${OBJECTDIR}/serial.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/serial.o.d" -o ${OBJECTDIR}/serial.o serial.c   
	
${OBJECTDIR}/eeprom.o: eeprom.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/eeprom.o.d 
	@${RM} ${OBJECTDIR}/eeprom.o 
	@${FIXDEPS} "${OBJECTDIR}/eeprom.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/eeprom.o.d" -o ${OBJECTDIR}/eeprom.o eeprom.c   
	
${OBJECTDIR}/check_gps_input.o: check_gps_input.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/check_gps_input.o.d 
	@${RM} ${OBJECTDIR}/check_gps_input.o 
	@${FIXDEPS} "${OBJECTDIR}/check_gps_input.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/check_gps_input.o.d" -o ${OBJECTDIR}/check_gps_input.o check_gps_input.c   
	
${OBJECTDIR}/gps_utils.o: gps_utils.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/gps_utils.o.d 
	@${RM} ${OBJECTDIR}/gps_utils.o 
	@${FIXDEPS} "${OBJECTDIR}/gps_utils.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/gps_utils.o.d" -o ${OBJECTDIR}/gps_utils.o gps_utils.c   
	
${OBJECTDIR}/gps_rx.o: gps_rx.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/gps_rx.o.d 
	@${RM} ${OBJECTDIR}/gps_rx.o 
	@${FIXDEPS} "${OBJECTDIR}/gps_rx.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/gps_rx.o.d" -o ${OBJECTDIR}/gps_rx.o gps_rx.c   
	
${OBJECTDIR}/uart_rx.o: uart_rx.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/uart_rx.o.d 
	@${RM} ${OBJECTDIR}/uart_rx.o 
	@${FIXDEPS} "${OBJECTDIR}/uart_rx.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/uart_rx.o.d" -o ${OBJECTDIR}/uart_rx.o uart_rx.c   
	
${OBJECTDIR}/error.o: error.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/error.o.d 
	@${RM} ${OBJECTDIR}/error.o 
	@${FIXDEPS} "${OBJECTDIR}/error.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/error.o.d" -o ${OBJECTDIR}/error.o error.c   
	
${OBJECTDIR}/parsefloat.o: parsefloat.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/parsefloat.o.d 
	@${RM} ${OBJECTDIR}/parsefloat.o 
	@${FIXDEPS} "${OBJECTDIR}/parsefloat.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/parsefloat.o.d" -o ${OBJECTDIR}/parsefloat.o parsefloat.c   
	
${OBJECTDIR}/acknowledge.o: acknowledge.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/acknowledge.o.d 
	@${RM} ${OBJECTDIR}/acknowledge.o 
	@${FIXDEPS} "${OBJECTDIR}/acknowledge.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/acknowledge.o.d" -o ${OBJECTDIR}/acknowledge.o acknowledge.c   
	
${OBJECTDIR}/check_uart_input.o: check_uart_input.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/check_uart_input.o.d 
	@${RM} ${OBJECTDIR}/check_uart_input.o 
	@${FIXDEPS} "${OBJECTDIR}/check_uart_input.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/check_uart_input.o.d" -o ${OBJECTDIR}/check_uart_input.o check_uart_input.c   
	
${OBJECTDIR}/setup_leds_oc.o: setup_leds_oc.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/setup_leds_oc.o.d 
	@${RM} ${OBJECTDIR}/setup_leds_oc.o 
	@${FIXDEPS} "${OBJECTDIR}/setup_leds_oc.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/setup_leds_oc.o.d" -o ${OBJECTDIR}/setup_leds_oc.o setup_leds_oc.c   
	
${OBJECTDIR}/get_waypoint.o: get_waypoint.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/get_waypoint.o.d 
	@${RM} ${OBJECTDIR}/get_waypoint.o 
	@${FIXDEPS} "${OBJECTDIR}/get_waypoint.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/get_waypoint.o.d" -o ${OBJECTDIR}/get_waypoint.o get_waypoint.c   
	
${OBJECTDIR}/distance.o: distance.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/distance.o.d 
	@${RM} ${OBJECTDIR}/distance.o 
	@${FIXDEPS} "${OBJECTDIR}/distance.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/distance.o.d" -o ${OBJECTDIR}/distance.o distance.c   
	
${OBJECTDIR}/game_timer.o: game_timer.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/game_timer.o.d 
	@${RM} ${OBJECTDIR}/game_timer.o 
	@${FIXDEPS} "${OBJECTDIR}/game_timer.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/game_timer.o.d" -o ${OBJECTDIR}/game_timer.o game_timer.c   
	
${OBJECTDIR}/hypot.o: hypot.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/hypot.o.d 
	@${RM} ${OBJECTDIR}/hypot.o 
	@${FIXDEPS} "${OBJECTDIR}/hypot.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/hypot.o.d" -o ${OBJECTDIR}/hypot.o hypot.c   
	
${OBJECTDIR}/smooth.o: smooth.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/smooth.o.d 
	@${RM} ${OBJECTDIR}/smooth.o 
	@${FIXDEPS} "${OBJECTDIR}/smooth.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/smooth.o.d" -o ${OBJECTDIR}/smooth.o smooth.c   
	
${OBJECTDIR}/set_leds_pct.o: set_leds_pct.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/set_leds_pct.o.d 
	@${RM} ${OBJECTDIR}/set_leds_pct.o 
	@${FIXDEPS} "${OBJECTDIR}/set_leds_pct.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/set_leds_pct.o.d" -o ${OBJECTDIR}/set_leds_pct.o set_leds_pct.c   
	
${OBJECTDIR}/erase.o: erase.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/erase.o.d 
	@${RM} ${OBJECTDIR}/erase.o 
	@${FIXDEPS} "${OBJECTDIR}/erase.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE) -g -D__DEBUG -D__MPLAB_DEBUGGER_ICD3=1 -fframe-base-loclist  -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/erase.o.d" -o ${OBJECTDIR}/erase.o erase.c   
	
else
${OBJECTDIR}/main.o: main.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/main.o.d 
	@${RM} ${OBJECTDIR}/main.o 
	@${FIXDEPS} "${OBJECTDIR}/main.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/main.o.d" -o ${OBJECTDIR}/main.o main.c   
	
${OBJECTDIR}/init.o: init.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/init.o.d 
	@${RM} ${OBJECTDIR}/init.o 
	@${FIXDEPS} "${OBJECTDIR}/init.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/init.o.d" -o ${OBJECTDIR}/init.o init.c   
	
${OBJECTDIR}/confbits.o: confbits.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/confbits.o.d 
	@${RM} ${OBJECTDIR}/confbits.o 
	@${FIXDEPS} "${OBJECTDIR}/confbits.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/confbits.o.d" -o ${OBJECTDIR}/confbits.o confbits.c   
	
${OBJECTDIR}/gps_led.o: gps_led.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/gps_led.o.d 
	@${RM} ${OBJECTDIR}/gps_led.o 
	@${FIXDEPS} "${OBJECTDIR}/gps_led.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/gps_led.o.d" -o ${OBJECTDIR}/gps_led.o gps_led.c   
	
${OBJECTDIR}/spi_rx.o: spi_rx.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/spi_rx.o.d 
	@${RM} ${OBJECTDIR}/spi_rx.o 
	@${FIXDEPS} "${OBJECTDIR}/spi_rx.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/spi_rx.o.d" -o ${OBJECTDIR}/spi_rx.o spi_rx.c   
	
${OBJECTDIR}/timer1_handler.o: timer1_handler.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/timer1_handler.o.d 
	@${RM} ${OBJECTDIR}/timer1_handler.o 
	@${FIXDEPS} "${OBJECTDIR}/timer1_handler.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/timer1_handler.o.d" -o ${OBJECTDIR}/timer1_handler.o timer1_handler.c   
	
${OBJECTDIR}/gps_button_handler.o: gps_button_handler.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/gps_button_handler.o.d 
	@${RM} ${OBJECTDIR}/gps_button_handler.o 
	@${FIXDEPS} "${OBJECTDIR}/gps_button_handler.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/gps_button_handler.o.d" -o ${OBJECTDIR}/gps_button_handler.o gps_button_handler.c   
	
${OBJECTDIR}/serial.o: serial.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/serial.o.d 
	@${RM} ${OBJECTDIR}/serial.o 
	@${FIXDEPS} "${OBJECTDIR}/serial.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/serial.o.d" -o ${OBJECTDIR}/serial.o serial.c   
	
${OBJECTDIR}/eeprom.o: eeprom.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/eeprom.o.d 
	@${RM} ${OBJECTDIR}/eeprom.o 
	@${FIXDEPS} "${OBJECTDIR}/eeprom.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/eeprom.o.d" -o ${OBJECTDIR}/eeprom.o eeprom.c   
	
${OBJECTDIR}/check_gps_input.o: check_gps_input.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/check_gps_input.o.d 
	@${RM} ${OBJECTDIR}/check_gps_input.o 
	@${FIXDEPS} "${OBJECTDIR}/check_gps_input.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/check_gps_input.o.d" -o ${OBJECTDIR}/check_gps_input.o check_gps_input.c   
	
${OBJECTDIR}/gps_utils.o: gps_utils.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/gps_utils.o.d 
	@${RM} ${OBJECTDIR}/gps_utils.o 
	@${FIXDEPS} "${OBJECTDIR}/gps_utils.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/gps_utils.o.d" -o ${OBJECTDIR}/gps_utils.o gps_utils.c   
	
${OBJECTDIR}/gps_rx.o: gps_rx.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/gps_rx.o.d 
	@${RM} ${OBJECTDIR}/gps_rx.o 
	@${FIXDEPS} "${OBJECTDIR}/gps_rx.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/gps_rx.o.d" -o ${OBJECTDIR}/gps_rx.o gps_rx.c   
	
${OBJECTDIR}/uart_rx.o: uart_rx.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/uart_rx.o.d 
	@${RM} ${OBJECTDIR}/uart_rx.o 
	@${FIXDEPS} "${OBJECTDIR}/uart_rx.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/uart_rx.o.d" -o ${OBJECTDIR}/uart_rx.o uart_rx.c   
	
${OBJECTDIR}/error.o: error.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/error.o.d 
	@${RM} ${OBJECTDIR}/error.o 
	@${FIXDEPS} "${OBJECTDIR}/error.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/error.o.d" -o ${OBJECTDIR}/error.o error.c   
	
${OBJECTDIR}/parsefloat.o: parsefloat.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/parsefloat.o.d 
	@${RM} ${OBJECTDIR}/parsefloat.o 
	@${FIXDEPS} "${OBJECTDIR}/parsefloat.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/parsefloat.o.d" -o ${OBJECTDIR}/parsefloat.o parsefloat.c   
	
${OBJECTDIR}/acknowledge.o: acknowledge.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/acknowledge.o.d 
	@${RM} ${OBJECTDIR}/acknowledge.o 
	@${FIXDEPS} "${OBJECTDIR}/acknowledge.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/acknowledge.o.d" -o ${OBJECTDIR}/acknowledge.o acknowledge.c   
	
${OBJECTDIR}/check_uart_input.o: check_uart_input.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/check_uart_input.o.d 
	@${RM} ${OBJECTDIR}/check_uart_input.o 
	@${FIXDEPS} "${OBJECTDIR}/check_uart_input.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/check_uart_input.o.d" -o ${OBJECTDIR}/check_uart_input.o check_uart_input.c   
	
${OBJECTDIR}/setup_leds_oc.o: setup_leds_oc.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/setup_leds_oc.o.d 
	@${RM} ${OBJECTDIR}/setup_leds_oc.o 
	@${FIXDEPS} "${OBJECTDIR}/setup_leds_oc.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/setup_leds_oc.o.d" -o ${OBJECTDIR}/setup_leds_oc.o setup_leds_oc.c   
	
${OBJECTDIR}/get_waypoint.o: get_waypoint.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/get_waypoint.o.d 
	@${RM} ${OBJECTDIR}/get_waypoint.o 
	@${FIXDEPS} "${OBJECTDIR}/get_waypoint.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/get_waypoint.o.d" -o ${OBJECTDIR}/get_waypoint.o get_waypoint.c   
	
${OBJECTDIR}/distance.o: distance.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/distance.o.d 
	@${RM} ${OBJECTDIR}/distance.o 
	@${FIXDEPS} "${OBJECTDIR}/distance.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/distance.o.d" -o ${OBJECTDIR}/distance.o distance.c   
	
${OBJECTDIR}/game_timer.o: game_timer.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/game_timer.o.d 
	@${RM} ${OBJECTDIR}/game_timer.o 
	@${FIXDEPS} "${OBJECTDIR}/game_timer.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/game_timer.o.d" -o ${OBJECTDIR}/game_timer.o game_timer.c   
	
${OBJECTDIR}/hypot.o: hypot.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/hypot.o.d 
	@${RM} ${OBJECTDIR}/hypot.o 
	@${FIXDEPS} "${OBJECTDIR}/hypot.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/hypot.o.d" -o ${OBJECTDIR}/hypot.o hypot.c   
	
${OBJECTDIR}/smooth.o: smooth.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/smooth.o.d 
	@${RM} ${OBJECTDIR}/smooth.o 
	@${FIXDEPS} "${OBJECTDIR}/smooth.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/smooth.o.d" -o ${OBJECTDIR}/smooth.o smooth.c   
	
${OBJECTDIR}/set_leds_pct.o: set_leds_pct.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/set_leds_pct.o.d 
	@${RM} ${OBJECTDIR}/set_leds_pct.o 
	@${FIXDEPS} "${OBJECTDIR}/set_leds_pct.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/set_leds_pct.o.d" -o ${OBJECTDIR}/set_leds_pct.o set_leds_pct.c   
	
${OBJECTDIR}/erase.o: erase.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} "${OBJECTDIR}" 
	@${RM} ${OBJECTDIR}/erase.o.d 
	@${RM} ${OBJECTDIR}/erase.o 
	@${FIXDEPS} "${OBJECTDIR}/erase.o.d" $(SILENT) -rsi ${MP_CC_DIR}../  -c ${MP_CC}  $(MP_EXTRA_CC_PRE)  -g -x c -c -mprocessor=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/erase.o.d" -o ${OBJECTDIR}/erase.o erase.c   
	
endif

# ------------------------------------------------------------------------------------
# Rules for buildStep: compileCPP
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
else
endif

# ------------------------------------------------------------------------------------
# Rules for buildStep: link
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
dist/${CND_CONF}/${IMAGE_TYPE}/urbancode.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}: ${OBJECTFILES}  nbproject/Makefile-${CND_CONF}.mk    
	@${MKDIR} dist/${CND_CONF}/${IMAGE_TYPE} 
	${MP_CC} $(MP_EXTRA_LD_PRE)  -mdebugger -D__MPLAB_DEBUGGER_ICD3=1 -mprocessor=$(MP_PROCESSOR_OPTION)  -o dist/${CND_CONF}/${IMAGE_TYPE}/urbancode.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX} ${OBJECTFILES_QUOTED_IF_SPACED}           -mreserve=data@0x0:0x1FC -mreserve=boot@0x1FC00490:0x1FC00BEF  -Wl,--defsym=__MPLAB_BUILD=1$(MP_EXTRA_LD_POST)$(MP_LINKER_FILE_OPTION),--defsym=__MPLAB_DEBUG=1,--defsym=__DEBUG=1,--defsym=__MPLAB_DEBUGGER_ICD3=1,-Map="${DISTDIR}/${PROJECTNAME}.${IMAGE_TYPE}.map"
	
else
dist/${CND_CONF}/${IMAGE_TYPE}/urbancode.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}: ${OBJECTFILES}  nbproject/Makefile-${CND_CONF}.mk   
	@${MKDIR} dist/${CND_CONF}/${IMAGE_TYPE} 
	${MP_CC} $(MP_EXTRA_LD_PRE)  -mprocessor=$(MP_PROCESSOR_OPTION)  -o dist/${CND_CONF}/${IMAGE_TYPE}/urbancode.X.${IMAGE_TYPE}.${DEBUGGABLE_SUFFIX} ${OBJECTFILES_QUOTED_IF_SPACED}          -Wl,--defsym=__MPLAB_BUILD=1$(MP_EXTRA_LD_POST)$(MP_LINKER_FILE_OPTION),-Map="${DISTDIR}/${PROJECTNAME}.${IMAGE_TYPE}.map"
	${MP_CC_DIR}\\xc32-bin2hex dist/${CND_CONF}/${IMAGE_TYPE}/urbancode.X.${IMAGE_TYPE}.${DEBUGGABLE_SUFFIX} 
endif


# Subprojects
.build-subprojects:


# Subprojects
.clean-subprojects:

# Clean Targets
.clean-conf: ${CLEAN_SUBPROJECTS}
	${RM} -r build/default
	${RM} -r dist/default

# Enable dependency checking
.dep.inc: .depcheck-impl

DEPFILES=$(shell mplabwildcard ${POSSIBLE_DEPFILES})
ifneq (${DEPFILES},)
include ${DEPFILES}
endif
