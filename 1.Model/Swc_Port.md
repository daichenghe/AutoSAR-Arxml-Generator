# BSW

| Sender /Server | Receiver /Client | S_Trigger | R_Trigger | Port type | Element(Structure/Array/Value) | Data type |
| -------------- | ---------------- | --------- | --------- | --------- | ------------------------------ | --------- |
| BSW       | ASW  	| 10ms  | R_Event   | SR    | HWI_V_CellU 				| Array 	|
| BSW       | ASW  	| 10ms  | 10ms      | SR  	| HWI_b_CellULineOpen 		| Array 	|
| BSW       | ASW  	| 10ms  | 10ms      | SR  	| HWI_deC_ChipT 			| Array 	|
| BSW       | ASW  	| 10ms  | 10ms      | SR  	| HWI_V_BoardT 				| Array 	|
| BSW       | ASW  	| 10ms  | 10ms      | SR  	| HWI_V_BattLv 				| Value 	|
| BSW       | ASW  	| 10ms  | 10ms      | SR  	| HWI_e_RlyPosSt 			| Value 	|
| BSW       | ASW  	| 10ms  | 10ms      | SR  	| HWI_e_RlyPreSt 			| Value 	|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_e_RlyHeatSt			| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_b_WakeUp				| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_inpd_flg_dataSaveOk	| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_e_SilentModSt			| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_e_WakeUpResRaw		| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_b_WkeUpBPS			| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_b_WakeUpSwt			| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_V_Crash				| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_Ohm_IotnR				| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_V_ChrgCnctAc			| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_V_ChrgCnctDc			| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_e_hvilSt				| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_V_BattCurr			| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_V_LinkMinusU			| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_V_LinkPlusU			| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_b_WkeUpAFE			| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_b_WkeUpBPSBoard		| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_V_BattCurrChk			| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_V_ShuntNTC			| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_Pa_BpsPressureBoard	| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_V_IsoGndRlyVolt		| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_V_IotnBrdVolt			| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_b_IsoGndRlyVoltInvlid	| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_b_IotnBrdVoltInvlid	| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_e_HvilDutyCycle		| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_V_AntiExpTemp			| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_Hz_HvilFrequency		| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_b_CellULineOpen		| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_V_BoardT				| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_cnt_CellUCrc			| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_cnt_CellUCrcBsw		| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_cnt_CellUCntr			| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_cnt_CellTCrc			| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_cnt_CellTCrcBsw		| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_b_CellTOverT			| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_V_CellT				| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWI_e_EOLRlyCmd			| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWERI_b_BattUVld			| Value		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWERI_b_CellTShoToVccOrOp	| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWERI_b_CellTShoToGnd		| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWERI_b_CellBalErr		| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWERI_b_CellUOverU		| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWERI_b_CellUUnderU		| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWERI_b_ChipComErr		| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| HWERI_b_SysRstErr			| Array		|
| BSW		| ASW	| 10ms	| 10ms		| SR	| AccRateType				| Structure	|

# ASW

| Sender /Server | Receiver /Client | S_Trigger | R_Trigger | Port type | Element(Structure/Array/Value) | Data type |
| -------------- | ---------------- | --------- | --------- | --------- | ------------------------------ | --------- |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_b_RlyPreCtrl      	| Value     |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_b_RlyHeatCtrl      	| Value     |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_e_RlyPosCtrl      	| Value     |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_b_1F0En      			| Value     |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_b_CMUSleepReq      	| Value     |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_V_CellUOverThdShtDw   | Value     |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_b_SocSaveReq      	| Value     |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_b_BcuShtDwnReq      	| Value     |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_b_IsoPosSwt      		| Value     |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_b_IsoMinusSwt      	| Value     |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_b_IsoGndSwt      		| Value     |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_b_BalCtrl      		| Array     |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_b_CellUActv      		| Array     |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_b_CellTActv      		| Array     |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_V_CellUUnderThdShtDw  | Array     |
| ASW    	| BSW 	| 10ms	| 10ms  | SR        | HWO_deC_CellTOverThdShtDw | Array     |
