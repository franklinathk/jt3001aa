# Specify specific item names
ITEMS_INA228 = [
              ('0x00 CONFIG',        '00', 'WR', ''),
              ('0xt1 ADC_CONFIG_H',  'aa', 'WR', ''),
              ("0xt2 ADC_CONFIG_L",  '82','WR', ''),
              ('0x02 SHUNT_CAL      ',  '00', 'WR', ''),
              ('0x03 SHUNT_TEMPCO   ',  'a5', 'R', ''),
              ('0x04 VSHUNT         ',  '80', 'R', ''),
              ('0x05 VBUS           ',  'b0', 'R', ''),
              ('0x06 DIETEMP        ',  '00', 'R', ''),
              ('0x07 CURRENT        ',  '00', 'R', ''),
              ('0x08 POWER          ',  '08', 'R', ''),
              ('0x09 ENERGY         ',  '00', 'R', ''),
              ('0x0A CHARGE         ',  '01', 'R', ''),
              ('0x0B DIAG_ALRT      ',  '00', 'R', ''),
              ('0x0C SOVL           ',  '02', 'R', ''),
              ('0x0D SUVL           ',  '00', 'R', ''),
              ('0x0E BOVL           ',  '03', 'R', ''),
              ('0x0F BUVL           ',  '00', 'R', ''),
              ('0x10 TEMP_LIMIT     ',  '04', 'R', ''),
              ('0x11 PWR_LIMIT      ',  '00', 'R', ''),
              ('0x3E MANUFACTURE_ID ',  '05', 'R', ''),
              ('0x3F DEVICE_ID      ',  '00', 'R', ''),
              ("OP12 INA228_exist", 'Yes','',{"Yes", "No"}),
              ("OP10 test_led_channel", '1','',{"1", "2","3","4","5", "6","7","8"}),
              ("OP11 PAM or PWM", 'PWM','',{"PWM", "PAM"}),
              ("OP13 TI_MAX_CURRENT", '0.005','',{"0.005","0.015","0.025","0.035"}),
              ("OP14 TI_RESISTOR", '1.0','',{"1.0","0.1","0.01"}),
              ("0xt3 HT2_or_DAC NUM",'1','WR', ''), 
              ("SW24 GET_LED_CURRENT",'','', ''), 
]
# Specify Settings item names
ITEMS_SETTINGS  = [
              ("SW02 AUTO SEND CMD", '','', ''), 
              ("SW03 VPP to 10V", '',''   , ''), 
              ("SW04 VDD to 5V", '',''    , ''), 
              ("SW06 CHOP_FREQ_TEST",'','', ''), 
              ("SW07 on_line Calibr",'','', ''), 
              ("SW08 LOCK",'','', ''), 
              ("OP02 DC low count", '0','', {"-2","-1","0","+1","+2"}), 
              ("OP04 DB low count", '0','', {"-1","0","+1","+2", "+3"}), 
              ("OP05 DB frame rate", '90Hz','', {"30Hz","90Hz","120Hz","240Hz"}), 
              ("OP06 DC Reset bit", '3','', {"2","3","4","5"}), 
              ("SW18 DC RESET",'','', ''), 
              ("OP07 DB Reset Bit", '4','', {"2","3","4","5"}), 
              ("SW23 DB RESET",'','', ''), 
              ("SW20 DB Repeat",'','', ''), 
              ("SW15 PRINT_MESSAGE",'','', ''), 
              ("SW16 ExtClk Enable",'','', ''), 
              ("SW17 OSC div256 Enable",'','',''), 
              ("SW21 NEW LINE ON CMD",'','',''), 
              ("OP09 test_osc_source", 'dbo','',{"dbo", "db","dc","62.915M"}),
            #  ("OP12 INA228_exist", 'Yes','',{"Yes", "No"}),
            #  ("OP10 test_led_channel", '1','',{"1", "2","3","4","5", "6","7","8"}),
            #  ("OP11 PAM or PWM", 'PWM','',{"PWM", "PAM"}),
            #  ("OP13 TI_MAX_CURRENT", '0.005','',{"0.005","0.015","0.025","0.035"}),
            #  ("OP14 TI_RESISTOR", '1.0','',{"1.0","0.1","0.01"}),
            #  ("0xt1 TI_ADC_CONFIG_H",'aa','WR', ''),
            #  ("0xt2 TI_ADC_CONFIG_L",'82','WR', ''),
            #  ("0xt3 HT2_or_DAC NUM",'1','WR', ''), 
            #   ("SW24 GET_LED_CURRENT",'','', ''), 
]

# Specify specific item names
ITEMS_OTP  = [("0x60 REG_PAG1", '00', 'WR', ''), 
              ("0x61 REG_PAG2", '00', 'WR', ''), 
              ("0x62 OSC_ADJ[4:0]", '10', 'WR', ''), 
              ("0x63 ADJ_IRA[2:0]", '04', 'WR', ''), 
              ("0x64 ADJ_TEMP[3:0]", '08', 'WR', ''), 
              ("0x65 VREF_TRIM[3:0]", '08', 'WR', ''), 
              ("0x66 CHOP_FREQ[1:0]", '01', 'WR', ''), 
              ("0x67 blk_pwm10_ditcut", '00', 'WR', ''), 
              ("0x68 ILED_TRIM1[6:0]", '40', 'WR', ''), 
              ("0x69 ILED_TRIM2[6:0]", '40', 'WR', ''), 
              ("0x6A ILED_TRIM3[6:0]", '40', 'WR', ''), 
              ("0x6B ILED_TRIM4[6:0]", '40', 'WR', ''), 
              ("0x6C ILED_TRIM5[6:0]", '40', 'WR', ''), 
              ("0x6D ILED_TRIM6[6:0]", '40', 'WR', ''), 
              ("0x6E ILED_TRIM7[6:0]", '40', 'WR', ''), 
              ("0x6F ILED_TRIM8[6:0]", '40', 'WR', ''), 
              ("0x70 MCSV2i_TRIM[3:0]", '07', 'WR', ''), 
              ("SW02 AUTO SEND CMD", '','', ''), 
              ("SW01 ENGINEER MODE", '','', ''), 
              ("0xbb_WRITE_READ_ALL",'00','WR', ''), 
              ]

jt3001_entries = [
              ('',''),
              ('CURRENT   :', 'Entry'),
              ('VBus      :', 'Entry'),
              ('Temperture:', 'Entry'),
]

tmp421_reges = [
              ('',''),
              ('x00 local temp (high byte) :', 'Entry'),
              ('x01 remote temp 1 (high byte) :', 'Entry'),
              ('x02 remote temp 2 (high byte) :', 'Entry'),
              ('x03 remote temp 3 (high byte) :', 'Entry'),
              ('X08 Status Register :', 'Entry'),
              ('X09 Configure Reg 1 :', 'Entry'),
              ('X0A Configure Reg 2 :', 'Entry'),
              ('X0B Conversion Rate :', 'Entry'),
              ('X10 Local temp (low byte) : ', 'Entry'),
              ('X11 remote temp 1 (low byte) :', 'Entry'),
              ('X12 remote temp 2 (low byte) :', 'Entry'),
              ('X13 remote temp 3 (low byte) :', 'Entry'),
              ('XFE Manufacture ID:', 'Entry'),
              ('XFF TEMP421 DEVICE_ID :', 'Entry'),
]

labels_entries = [
              ('',''),
              ('x00 CONFIG    :', 'Entry'),
           #   ('x01 ADC_CONFIG:', f'Entry {current_value} mA'),
              ('x01 ADC_CONFIG:', 'Entry'),
              ('x02 SHUNT_CAL :', 'Entry'),
              ('x03 SHUNT_TEMPCO :', 'Entry'),
              ('x04 VSHUNT :', 'Entry'),
              ('X05 VBUS :', 'Entry'),
              ('X06 DIETEMP :', 'Entry'),
              ('X07 CURRENT :', 'Entry'),
              ('X08 POWER :', 'Entry'),
              ('X09 ENERGY :', 'Entry'),
              ('X0A CHARGE:', 'Entry'),
              ('X0B DIAG_ALRT:', 'Entry'),
              ('X0C SOVL :', 'Entry'),
              ('X0D SUVL :', 'Entry'),
              ('X0E BOVL :', 'Entry'),
              ('X0F BUVL :', 'Entry'),
              ('X10 TEMP_LIMIT:', 'Entry'),
              ('X11 PWR_LIMIT :', 'Entry'),
              ('X3E MANUFACTURE_ID :', 'Entry'),
              ('X3F DEVICE_ID :', 'Entry'),
]

ITEMS_VOL_CUR = [ 
              ("0xv2 iteration Set",'5','WR', ''), 
              ("SW10 VREF TRIM",'','', ''), 
              ("0xcd VOLTAGE",'0000','000000', '00'), 
              ("SW11 CURRENT TRIM",'','', ''), 
              ("OP08 CURRENT MAX", '15mA','', {"35mA","25mA","15mA","5mA"}), 
              ("0xc1 LED CHANNEL 1",'0000000','000000', '00'), 
              ("0xc2 LED CHANNEL 2",'0000000','000000', '00'), 
              ("0xc3 LED CHANNEL 3",'0000000','000000', '00'), 
              ("0xc4 LED CHANNEL 4",'0000000','000000', '00'), 
              ("0xc5 LED CHANNEL 5",'0000000','000000', '00'), 
              ("0xc6 LED CHANNEL 6",'0000000','000000', '00'), 
              ("0xc7 LED CHANNEL 7",'0000000','000000', '00'), 
              ("0xc8 LED CHANNEL 8",'0000000','000000', '00'), 
              ("0xc9 COARSE FREQ",'000010','000100', '00'), 
              ("0xca Measured Corse FREQ", '00Mhz','',''),
              ("0xcb FINE FREQ",'001010','000000', '00'), 
              ("0xcc Measured Fine FREQ",'00Mhz','', ''), 
              ("SW13 FREQ COARSE TRIM",'','', ''), 
              ("SW14 FREQ FINETUNE TRIM",'','', ''), 
              ("SW19 AVDDL from DBO",'','', ''), 
              ("SW22 AUTO SEARCH FREQ",'','', ''), 
            ]
# Specify specific item names
ITEMS_DC = [ 
              ("0x00 READ_NUM     ", '01', "WR", '' ), 
              ("0x01 DIMM_ID      ", '01', "WR", '' ), 
              ("0x28 VDL_ERR      ", '00', "R" , ''), 
              ("0x29 CRCDCDB_OTP  ", '00', 'R' , ''), 
              ("0x2A OPEN_ERR     ", '00', 'R' , ''), 
              ("0x2B SHORT_ERR    ", '00', 'R' , ''), 
              ("0x2D DCDBOI_ERR   ", '00', 'R' , ''), 
              ("0x30 CH_ENABLE    ", 'FF', 'WR', '' ), 
              ("0x31 EN_TUSOD     ", '08', 'WR', '' ),
              ("0x32 AC_UOS_LP    ", '00', 'WR', '' ), 
              ("0x33 SW_OTP_OHP   ", 'a5', 'WR', '' ), 
              ("0x34 MODE_CLK_SEL ", '80', 'WR', '' ), 
              ("0x35 TH_IDACG     ", 'b0', 'WR', '' ), 
              ("0x36 RST_REMAP    ", '00', 'WR', '' ), 
              ("0x37 DBCRC_BYPS   ", '00', 'WR', '' ), 
              ("0x3A HSC_NUM[7:0] ", 'FF', 'WR', '' ), 
              ("0x3B HSC_NUM[15:8]", '0F', 'WR', '' ), 
              ("0x3C PS1[7:0]"     , '01', 'WR', '' ), 
              ("0x3D PS1[11:8]"    , '00', 'WR', '' ), 
              ("0x3E PS2[7:0]"     , '02', 'WR', '' ), 
              ("0x3F PS2[11:8]"    , '00', 'WR', '' ), 
              ("0x40 PS3[7:0]"     , '03', 'WR', '' ), 
              ("0x41 PS3[11:8]"    , '00', 'WR', '' ), 
              ("0x42 PS4[7:0]"     , '04', 'WR', '' ), 
              ("0x43 PS4[11:8]"    , '00', 'WR', '' ), 
              ("0x44 PS5[7:0]"     , '05', 'WR', '' ), 
              ("0x45 PS5[11:8]"    , '00', 'WR', '' ), 
              ("0x46 PS6[7:0]"     , '06', 'WR', '' ), 
              ("0x47 PS6[11:8]"    , '00', 'WR', '' ), 
              ("0x48 PS7[7:0]"     , '07', 'WR', '' ), 
              ("0x49 PS7[11:8]"    , '00', 'WR', '' ), 
              ("0x4A PS8[7:0]"     , '08', 'WR', '' ), 
              ("0x4B PS8[11:8]"    , '00', 'WR', '' ), 
              ("0x4C DCDB_SPEED"   , '03', 'WR', '' ), 
              ("0x4D LOCK_BYTE"    , 'a5', 'WR', '' )  
        ]

# Specify specific item names
ITEMS_DB = [  ("0x00_Product_ID",  '08', "R", ''  ), # use bit_cnt_pulse to trigger 
              ("0x01_DIM_ADDRES",  '01', "WR", '' ), # byte_rx_cn : 1b
              #("0x10_IDAC1[7:0]",  '00', "WR", '' ), # byte_rx_cn : 1a
              ("0x10_IDAC1[7:0]",  'ff', "WR", '' ), # byte_rx_cn : 1a
              ("0x11___HT1[7:0]",  '00', 'WR', '' ), # byte_rx_cn : 19 
              ("0x12__HT1[15:8]",  'f0', 'WR', '' ), # byte_rx_cn : 18 
              #("0x13_IDAC2[7:0]",  '00', 'WR', '' ), # byte_rx_cn : 17 
              ("0x13_IDAC2[7:0]",  'f0', 'WR', '' ), # byte_rx_cn : 17 
              ("0x14___HT2[7:0]",  '01', 'WR', '' ), # byte_rx_cn : 16 
              ("0x15__HT2[15:8]",  '80', 'WR', '' ), # byte_rx_cn : 15 
              ("0x16_IDAC3[7:0]",  '00', 'WR', '' ), # byte_rx_cn : 14
              #("0x16_IDAC3[7:0]",  'ff', 'WR', '' ), # byte_rx_cn : 14
              ("0x17___HT3[7:0]",  '02', 'WR', '' ), # byte_rx_cn : 13 
              ("0x18__HT3[15:8]",  '80', 'WR', '' ), # byte_rx_cn : 12 
              ("0x19_IDAC4[7:0]",  '00', 'WR', '' ), # byte_rx_cn : 11 
              #("0x19_IDAC4[7:0]",  'ff', 'WR', '' ), # byte_rx_cn : 11 
              ("0x1A___HT4[7:0]",  '03', 'WR', '' ), # byte_rx_cn : 10 
              ("0x1B__HT4[15:8]",  '80', 'WR', '' ), # byte_rx_cn : 0f 
              ("0x1C_IDAC5[7:0]",  '00', 'WR', '' ), # byte_rx_cn : 0e 
              #("0x1C_IDAC5[7:0]",  'ff', 'WR', '' ), # byte_rx_cn : 0e 
              ("0x1D___HT5[7:0]",  '04', 'WR', '' ), # byte_rx_cn : 0d
              ("0x1E__HT5[15:8]",  '80', 'WR', '' ), # byte_rx_cn : 0c
              ("0x1F_IDAC6[7:0]",  '00', 'WR', '' ), # byte_rx_cn : 0b
              #("0x1F_IDAC6[7:0]",  'ff', 'WR', '' ), # byte_rx_cn : 0b
              ("0x20___HT6[7:0]",  '05', 'WR', '' ), # byte_rx_cn : 0a
              ("0x21__HT6[15:8]",  '80', 'WR', '' ), # byte_rx_cn : 09
              ("0x22_IDAC7[7:0]",  '00', 'WR', '' ), # byte_rx_cn : 08
              #("0x22_IDAC7[7:0]",  'ff', 'WR', '' ), # byte_rx_cn : 08
              ("0x23___HT7[7:0]",  '06', 'WR', '' ), # byte_rx_cn : 07 
              ("0x24__HT7[15:8]",  '80', 'WR', '' ), # byte_rx_cn : 06
              ("0x25_IDAC8[7:0]",  '00', 'WR', '' ), # byte_rx_cn : 05
              #("0x25_IDAC8[7:0]",  'ff', 'WR', '' ), # byte_rx_cn : 05
              ("0x26___HT8[7:0]",  '07', 'WR', '' ), # byte_rx_cn : 04
              ("0x27__HT8[15:8]",  '80', 'WR', '' ), # byte_rx_cn : 03
              ("0xaa__WRITE_READ_ALL",'00','WR', ''), 
         ]                              