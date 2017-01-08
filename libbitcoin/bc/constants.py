from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.string_ import String

user_agent = str(ffi.string(lib.bc_user_agent()), "utf-8")

min_int64 = lib.bc_min_int64()
max_int64 = lib.bc_max_int64()
min_int32 = lib.bc_min_int32()
max_int32 = lib.bc_max_int32()
max_uint64 = lib.bc_max_uint64()
max_uint32 = lib.bc_max_uint32()
max_uint16 = lib.bc_max_uint16()
max_uint8 = lib.bc_max_uint8()
max_size_t = lib.bc_max_size_t()
byte_bits = lib.bc_byte_bits()
no_previous_output = lib.bc_no_previous_output()
max_input_sequence = lib.bc_max_input_sequence()
sighash_null_value = lib.bc_sighash_null_value()
max_number_size = lib.bc_max_number_size()
max_cltv_number_size = lib.bc_max_cltv_number_size()
max_counted_ops = lib.bc_max_counted_ops()
max_stack_size = lib.bc_max_stack_size()
max_script_size = lib.bc_max_script_size()
max_push_data_size = lib.bc_max_push_data_size()
max_script_public_key_count = lib.bc_max_script_public_key_count()
multisig_default_sigops = lib.bc_multisig_default_sigops()
max_null_data_size = lib.bc_max_null_data_size()
min_coinbase_size = lib.bc_min_coinbase_size()
max_coinbase_size = lib.bc_max_coinbase_size()
median_time_past_interval = lib.bc_median_time_past_interval()
max_block_size = lib.bc_max_block_size()
max_block_sigops = lib.bc_max_block_sigops()
coinbase_maturity = lib.bc_coinbase_maturity()
time_stamp_future_hours = lib.bc_time_stamp_future_hours()
locktime_threshold = lib.bc_locktime_threshold()
proof_of_work_limit = lib.bc_proof_of_work_limit()
retargeting_factor = lib.bc_retargeting_factor()
target_spacing_seconds = lib.bc_target_spacing_seconds()
double_spacing_seconds = lib.bc_double_spacing_seconds()
target_timespan_seconds = lib.bc_target_timespan_seconds()
min_timespan = lib.bc_min_timespan()
max_timespan = lib.bc_max_timespan()
retargeting_interval = lib.bc_retargeting_interval()
bip65_version = lib.bc_bip65_version()
bip66_version = lib.bc_bip66_version()
bip34_version = lib.bc_bip34_version()
first_version = lib.bc_first_version()
testnet_active = lib.bc_testnet_active()
testnet_enforce = lib.bc_testnet_enforce()
testnet_sample = lib.bc_testnet_sample()
mainnet_active = lib.bc_mainnet_active()
mainnet_enforce = lib.bc_mainnet_enforce()
mainnet_sample = lib.bc_mainnet_sample()
bip16_activation_time = lib.bc_bip16_activation_time()
command_size = lib.bc_command_size()
max_get_blocks = lib.bc_max_get_blocks()
max_get_headers = lib.bc_max_get_headers()
max_get_data = lib.bc_max_get_data()
max_inventory = lib.bc_max_inventory()
varint_two_bytes = lib.bc_varint_two_bytes()
varint_four_bytes = lib.bc_varint_four_bytes()
varint_eight_bytes = lib.bc_varint_eight_bytes()
string_terminator = lib.bc_string_terminator()
satoshi_per_bitcoin = lib.bc_satoshi_per_bitcoin()
initial_block_reward_bitcoin = lib.bc_initial_block_reward_bitcoin()
initial_block_reward_satoshi = lib.bc_initial_block_reward_satoshi()
reward_interval = lib.bc_reward_interval()
recursive_money = lib.bc_recursive_money()
max_money = lib.bc_max_money()

