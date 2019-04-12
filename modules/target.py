"""Module: Target"""

import os

from app import const
from modules import file
from modules import log
from modules import runner


# -----------------------------------------------------------------------------
def get_all_targets(proj_path):
    results = []

    targets_path = os.path.join(
        proj_path,
        const.DIR_NAME_FILES,
        const.DIR_NAME_FILES_TARGETS,
    )

    if not os.path.isdir(targets_path):
        log.error('Target folder not exists: {0}'.format(targets_path))

    targets = file.find_dirs_simple(targets_path, '*')

    if targets:
        for target_path in targets:
            target_name = os.path.basename(target_path)

            if target_name:
                results.append(target_name)

    results.sort()

    return results


# -----------------------------------------------------------------------------
def get_all_target_verbs(proj_path, target_name):
    results = []

    target_verbs_list = file.find_files_simple(os.path.join(
        proj_path,
        const.DIR_NAME_FILES,
        const.DIR_NAME_FILES_TARGETS,
        target_name,
        const.DIR_NAME_FILES_TARGET_VERBS,
    ), '*.py')

    if target_verbs_list:
        for verb_file in target_verbs_list:
            verb_name = os.path.basename(verb_file)
            verb_name = os.path.splitext(verb_name)[0]

            if verb_name:
                results.append(verb_name)

    results.sort()
    return results


# -----------------------------------------------------------------------------
def get_target_config(proj_path, target_name):
    config_folder = os.path.join(
        proj_path,
        const.DIR_NAME_FILES,
        const.DIR_NAME_FILES_CONFIG,
    )

    module_name = 'target_{0}'.format(target_name)

    target_config_file = os.path.join(
        config_folder,
        module_name,
    )

    if file.file_exists(target_config_file):
        return runner.run_external(
            path=config_folder,
            module_name=module_name,
            command_name='run',
            command_params={},
            show_log=False,
            show_error_log=True,
            throw_error=True,
        )

    return {}
