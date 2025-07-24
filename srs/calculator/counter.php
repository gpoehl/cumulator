<?php

/**
 * Simple calculator for counters
 *
 * @author Günter Pöhl
 */
declare(strict_types=1);

namespace gpoehl\cumulator\calculator;

use gpoehl\cumulator\calculator\BaseCalculator;

class Counter extends BaseCalculator {

    public function __construct(public readonly int $maxLevel = 0) {
        if ($maxLevel < 0) {
            throw new \InvalidArgumentException("maxLevel can't be negative ($maxLevel given).");
        }
        $this->initialize();
    }

    private function initialize(): void {
        $this->total = array_fill(0, $this->maxLevel + 1, 0);
    }

    #[\Override]
    public function setInitialValue(int $level, int $value): void {
        $this->total[$level] = $value;
    }

    #[\Override]
    public function cumulate(int $level): void {
        $this->total[$level - 1] += $this->total[$level];
        $this->total[$level] = 0;
    }

    public function increment(): void {
        $this->total[$this->maxLevel]++;
    }

    public function decrement(): void {
        $this->total[$this->maxLevel]--;
    }

    #[\Override]
    public function add(int $value): void {
        $this->total[$this->maxLevel] += $value;
    }

    #[\Override]
    public function sub(int $value): void {
        $this->total[$this->maxLevel] -= $value;
    }

    #[\Override]
    public function sum(int $level): int {
        return array_sum(array_slice($this->total, $level));
    }
}
