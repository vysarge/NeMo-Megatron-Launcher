import os


BASE_RESULTS_DIR = os.environ.get("RESULTS_DIR")

class TestCIGPT126m:

    def test_ci_data_prep_t5_the_pile_shard00(self):
        idx_path = os.path.join(BASE_RESULTS_DIR, "data/my-t5_00_text_document.idx")
        bin_path = os.path.join(BASE_RESULTS_DIR, "data/my-t5_00_text_document.bin")
        assert os.path.exists(idx_path), f"File not found: {idx_path}"
        assert os.path.exists(bin_path), f"File not found: {bin_path}"
