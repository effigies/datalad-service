from datalad_service.common.annex import CommitInfo, get_repo_files
from datalad_service.common.celery import dataset_task
from datalad_service.common.celery import app


@dataset_task
def commit_files(store, dataset, files, email=None, name=None):
    ds = store.get_dataset(dataset)
    with CommitInfo(ds, email, name):
        for filename in files:
            ds.add(filename)


@dataset_task
def unlock_files(store, dataset, files):
    ds = store.get_dataset(dataset)
    for filename in files:
        ds.unlock(filename)


@dataset_task
def get_files(store, dataset, branch=None):
    ds = store.get_dataset(dataset)
    return get_repo_files(ds, branch)