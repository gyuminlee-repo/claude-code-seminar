"""TODO: RBS strength vs GFP intensity fit.

지난주에 시작했다가 plate reader 결과 기다리느라 멈춤.
일단 de_results.csv 로 컬럼 구조만 훑어봄.
"""
import csv
import logging

logger = logging.getLogger(__name__)

path = "data/de_results.csv"

with open(path, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

logger.info("rows: %d", len(rows))
if rows:
    logger.info("cols: %s", list(rows[0].keys()))

# TODO: 실제 fit. scipy.optimize.curve_fit 쓸지 sklearn linear 쓸지 결정.
# 여기까지. plate reader 결과 들어오면 다시.
